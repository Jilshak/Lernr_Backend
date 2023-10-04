import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from courses.models import Courses

@api_view(['POST'])
def create_payment_session(request):
    info = request.data
    course_id = info['course_id']

    course = Courses.objects.get(id=course_id)
    stripe_product_id = course.stripe_product_id

    price = stripe.Price.list(product=stripe_product_id, limit=1)

    if price.data:
        price_id = price.data[0].id

        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=price.data[0].unit_amount,
                currency=price.data[0].currency,
                payment_method_types=['card'],
                description=f'Payment for course: {course.title}',
                statement_descriptor='Your Course',
            )

            # Check the payment intent state
            payment_intent_response = stripe.PaymentIntent.retrieve(payment_intent.id)
            if payment_intent_response.status != 'created' and payment_intent_response.status != 'requires_payment_method':
                raise Exception('Payment intent is not in a valid state.')

            # Create the session
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': price_id,
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://127.0.0.1:5173/test',
                cancel_url=f'http://127.0.0.1:5173/coursepage/{course_id}',
            )

            return Response(
                status=status.HTTP_200_OK,
                data={'session_id': session.id, 'pi':payment_intent_response.client_secret})
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={'error': str(e)})
    else:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={'error': 'No price found for the product.'})
