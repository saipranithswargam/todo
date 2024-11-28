from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    subject = "Welcome to Todos App"
    message = "Thank you for registering! We're excited to have you on board."
    from_email = "no-reply@todosapp.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Welcome email sent to {email}"
