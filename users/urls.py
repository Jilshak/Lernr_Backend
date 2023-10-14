from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import UserViewSet, MyTokenObtainPairView
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ChangePasswordView, request_password_reset, confirm_password_reset

router = DefaultRouter()
router.register('user', UserViewSet, basename='user_view')


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('request-password-reset/', request_password_reset, name='request-passwprd-reset'),
    path('confirm-password-reset/', confirm_password_reset, name='confirm-passwprd-reset'),
]

urlpatterns += router.urls
