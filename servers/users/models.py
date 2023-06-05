from django.db import models
from django.contrib.auth.models import User

MAX_LENGTH_APP_USER_ID = 16

def create_unique_appuser_id():
    from secrets import token_hex
    secret = None
    while (not secret) or (AppUser.objects.filter(unique_id=secret).first()):
        secret = token_hex(MAX_LENGTH_APP_USER_ID // 2)
    
    return secret

# Create your models here.
class AppUser(models.Model):
    user = models.OneToOneField(to=User, null=True, blank=True, on_delete=models.SET_NULL, related_name="app_user")
    unique_id = models.CharField(max_length=MAX_LENGTH_APP_USER_ID, default=create_unique_appuser_id, db_index=True, unique=True)
    