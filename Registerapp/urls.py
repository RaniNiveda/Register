#author raniniveda
from rest_framework.routers import DefaultRouter
from .views import RegisterUserView
from django.urls import path,include
from rest_framework.authtoken import views

router=DefaultRouter()
router.register('users',RegisterUserView,base_name='users')

urlpatterns=[
	path('',include(router.urls)),
	path('api-token-auth/',views.obtain_auth_token,name='token')
	]