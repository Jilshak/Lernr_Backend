from django.urls import path
from .views import create_payment_session, create_cart_payment_session

urlpatterns = [
    path('stripe/', create_payment_session),
    path('stripe_cart/', create_cart_payment_session)
]