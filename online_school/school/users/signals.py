from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.tasks import auto_activate_user, send_welcome_email


@receiver(post_save, sender=get_user_model())
def user_post_save(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        auto_activate_user.delay(instance.id)
        send_welcome_email.delay(instance.id)
