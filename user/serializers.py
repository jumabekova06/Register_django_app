from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            "username",
            "email",
            "phone",
            "password",

        ]

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            "username",
            "email",
            "phone",
            # "password",

        ]
