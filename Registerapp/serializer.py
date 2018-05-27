#author raniniveda
from rest_framework import serializers
from .models import RegisterUser

class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
            user = RegisterUser.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                mobile_number=validated_data['mobile_number'],
                password=validated_data['password'],
                gender=validated_data['gender']
            )

            user.set_password(validated_data['password'])
            user.save()
            return user
    class Meta:
        model = RegisterUser
        fields = ('email', 'username','mobile_number','gender','password')
        write_only_fields=('password',)
