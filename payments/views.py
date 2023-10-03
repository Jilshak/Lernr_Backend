import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@api_view(['POST'])
def test_payment(request):
    info = request.data
    amount_in_cents = int(info['price'] * 100)
    test_payment_intent = stripe.PaymentIntent.create(
        amount=amount_in_cents,
        currency='inr',
        payment_method_types=['card',],
        receipt_email=info['email']
    )
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)

@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        data = request.json()
        payment_method_id = data.get('paymentMethodId')

        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            payment_intent = stripe.PaymentIntent.confirm(
                payment_method=payment_method_id,
                confirm=True,
                amount=data.get('price'),
                currency='inr',
                description='Payment for Order #123',
            )
            return JsonResponse({'message': 'Payment successful'})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})