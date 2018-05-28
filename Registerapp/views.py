#author raniniveda
from rest_framework import viewsets
from .models import RegisterUser
from . import serializer
from rest_framework.permissions import AllowAny

class RegisterUserView(viewsets.ModelViewSet):
	queryset= RegisterUser.objects.all()
	serializer_class=serializer.RegisterSerializer
	permission_classes=(AllowAny,)

# Create your views here.
