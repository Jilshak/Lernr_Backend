from django.urls import path
from .views import create_checkout_session

urlpatterns = [
    path('test', create_checkout_session)
]