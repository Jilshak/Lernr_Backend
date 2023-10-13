import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from courses.models import Courses, CoursesBought, CartItem
from users.models import CustomUser


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
                amount=price.data[0].unit_amount * 100,
                currency=price.data[0].currency,
                payment_method_types=['card'],
                description=f'Payment for course: {course.title}',
                statement_descriptor='Your Course',
            )

            # Check the payment intent state
            payment_intent_response = stripe.PaymentIntent.retrieve(
                payment_intent.id)
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
                data={'session_id': session.id, 'pi': payment_intent_response.client_secret})
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={'error': str(e)})
    else:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={'error': 'No price found for the product.'})


@api_view(['POST'])
def create_cart_payment_session(request):
    try:
        info = request.data
        print("This is the info: ", info)
        course_ids = info.get('course_id', [])

        if not course_ids:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error': 'No courses in the cart.'}
            )

        courses = Courses.objects.filter(id__in=course_ids)
        if not courses.exists():
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'error': 'No valid courses found in the cart.'}
            )

        product_ids = [course.stripe_product_id for course in courses]
        prices = []

        for product_id in product_ids:
            price_list = stripe.Price.list(product=product_id, limit=1)
            if price_list.data:
                price = price_list.data[0]
                prices.append(price)

        total_amount = sum(price.unit_amount for price in prices) * 100

        stripe.api_key = settings.STRIPE_SECRET_KEY

        payment_intent = stripe.PaymentIntent.create(
            amount=total_amount,
            currency='inr',
            payment_method_types=['card'],
            description='Payment for multiple courses',
            statement_descriptor='Your Courses',
        )

        line_items = [{'price': price.id, 'quantity': 1} for price in prices]

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url='http://127.0.0.1:5173/success',
            cancel_url='http://127.0.0.1:5173/cart',
        )
        
        user =CustomUser.objects.get(id=info.get('user'))
        
        for course_id in course_ids:
            CoursesBought.objects.create(user=user, course_id=Courses.objects.get(id=course_id))
        
        for course_id in course_ids:
            CartItem.objects.filter(user=user, on_course=course_id).delete()
            
        

        return Response(
            status=status.HTTP_200_OK,
            data={'session_id': session.id, 'pi': payment_intent.client_secret}
        )
    except Exception as e:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            data={'error': str(e)}
        )
