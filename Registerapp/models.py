
#author raniniveda
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save,sender=settings.AUTH_USER_MODEL)

def create_auth_token(sender,instance=None,created=False,**kwargs):
	if created:
		Token.objects.create(user=instance)
		
class RegisterUser(AbstractUser):
    mobile_number = models.CharField(blank=True, max_length=10)
    gender=models.CharField(blank=True,max_length=10)
