from django.urls import path
from .views import create_payment_session

urlpatterns = [
    path('stripe/', create_payment_session)
]