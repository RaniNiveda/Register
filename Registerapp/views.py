#author raniniveda
from rest_framework import viewsets
from .models import RegisterUser
from . import serializer

class RegisterUserView(viewsets.ModelViewSet):
	queryset= RegisterUser.objects.all()
	serializer_class=serializer.RegisterSerializer

# Create your views here.
