from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_activation_mail(email, otp):
    activation_link = f'http://127.0.0.1:8000/api/users/activation/{otp}'
    html_message = render_to_string('email.html', {'activation_link': activation_link})
    plain_message = strip_tags(html_message)

    send_mail(
        'Account Activation',
        plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
        html_message=html_message
    )