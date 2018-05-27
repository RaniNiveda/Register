#author raniniveda
from rest_framework.routers import DefaultRouter
from .views import RegisterUserView
from django.urls import path,include

router=DefaultRouter()
router.register('users',RegisterUserView,base_name='users')

urlpatterns=[
	path('',include(router.urls)),
	]