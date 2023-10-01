from django.urls import path
from .views import StripeCheckoutView


urlpatterns = [
    path(r'test-payment/', StripeCheckoutView.as_view()),
]