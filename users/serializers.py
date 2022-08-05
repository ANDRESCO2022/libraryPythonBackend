from rest_framework import serializers

from .models import UserLibrary


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLibrary
        fields = "__all__"


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLibrary
        fields = ("email", "password", "first_name")
