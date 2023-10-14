# utils.py
import secrets
from django.core.mail import send_mail
from django.conf import settings

def generate_unique_token():
    return secrets.token_urlsafe(32)

def send_password_reset_email(email, token):
    subject = 'Password Reset'
    message = f'Click the following link to reset your password: http://localhost:5173/reset_password/{token}/'
    from_email = settings.EMAIL_FROM
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
