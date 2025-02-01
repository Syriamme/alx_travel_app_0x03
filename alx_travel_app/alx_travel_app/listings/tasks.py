# listings/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(email, booking_details):
    subject = "Booking Confirmation"
    message = f"Dear customer, your booking has been confirmed. Details: {booking_details}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
