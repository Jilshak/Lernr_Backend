from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, PasswordResetSerializer, ChangePasswordSerializer
from rest_framework.decorators import api_view
from .models import CustomUser, PasswordResetToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# for changing the password
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework import status
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from .utils import generate_unique_token, send_password_reset_email


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser
        token['is_instructor'] = user.is_instructor
        token['is_blocked'] = user.is_blocked
        token['username'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            new_password = serializer.validated_data['new_password']
            instance.set_password(new_password)
            instance.save()
            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def request_password_reset(request):
    serializer = PasswordResetSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        try:
            user = CustomUser.objects.get(email=email)
            token = generate_unique_token()
            PasswordResetToken.objects.create(user=user, token=token)
            send_password_reset_email(email, token)
            return Response({'message': 'Password reset email sent.'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def confirm_password_reset(request):
    token = request.data.get('token')
    new_password = request.data.get('new_password')
    try:
        reset_token = PasswordResetToken.objects.get(token=token)
        user = reset_token.user
        user.set_password(new_password)
        user.save()
        reset_token.delete()
        return Response({'message': 'Password reset successful.'}, status=status.HTTP_200_OK)
    except PasswordResetToken.DoesNotExist:
        return Response({'error': 'Invalid or expired token.'}, status=status.HTTP_400_BAD_REQUEST)
