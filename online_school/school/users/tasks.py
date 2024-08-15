import logging
from config.celery import app
from django.core.mail import send_mail
from django.contrib.auth import get_user_model


@app.task
def auto_activate_user(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        user.is_active = True
        user.save()
    except UserModel.DoesNotExist:
        logging.warning(f"Tried to activate non-existing user {user_id}")


@app.task
def send_welcome_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'Welcome to School!',
            'Thank you for creating an account at our school!',
            'from@online_school.dev',
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning(f"Tried to send email to non-existing user {user_id}")
