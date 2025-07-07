from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class CustomUserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "phone_number", "profile_picture", "user_type"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    profile_picture = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "phone_number", "user_type", "profile_picture", "password1", "password2")
        extra_kwargs = {"password1": {"write_only": True}, "password2": {"write_only": True}}

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match!"})
        validate_password(attrs['password1'])
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")
        user = CustomUser.objects.create_user(password=password, **validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data.get('email'), password=data.get('password'))
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials!")