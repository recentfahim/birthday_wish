from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError


class UserSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateTimeField(required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'date_of_birth']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user


class LoginSerializer(TokenObtainPairSerializer):
    username_field = CustomUser.EMAIL_FIELD

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:

            user = authenticate(email=email, password=password)

            if user:
                refresh = self.get_token(user)
                data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return data
            else:
                raise AuthenticationFailed({
                    'result': {
                        "detail": "Invalid email or password."
                    },
                    'success': False
                })

        raise serializers.ValidationError({
            'result': {
                "detail": "Email and password are required."
            },
            'success': False
        })


class RefreshTokenSerializer(TokenRefreshSerializer):
    def run_validation(self, data):
        try:
            return super().run_validation(data)
        except TokenError as e:
            raise serializers.ValidationError(str(e))