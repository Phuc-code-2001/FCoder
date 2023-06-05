from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from .models import AppUser

@receiver(post_save, sender=User)
def create_app_user_automatically(sender, instance, created, **kwargs):
    
    if created:
        AppUser.objects.create(user=instance)