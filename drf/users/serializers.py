# users/serializers.py
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = models.User.objects.create(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            birth_date=validated_data.get('birth_date')
        )

        user.set_password(validated_data.get('password'))
        user.save()

        return user

    class Meta:
        model = models.User
        fields = ('email', 'password', 'first_name', 'last_name', 'birth_date')
