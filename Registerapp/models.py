
#author raniniveda
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class RegisterUser(AbstractUser):
    mobile_number = models.CharField(blank=True, max_length=10)
    gender=models.CharField(blank=True,max_length=10)
