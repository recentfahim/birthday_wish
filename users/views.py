from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer, RefreshTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            if CustomUser.objects.filter(email=request.data.get('email')).count() > 0:
                user_serializer.save()
                context = {
                    'result': {
                        "message": "Your account has been created."
                        },
                    'success': True
                }
                return Response(context, status=status.HTTP_201_CREATED)
            else:
                context = {
                    'result': {
                        "message": "An account already exists with this email"
                    },
                    'success': False
                }
                return Response(context, status=status.HTTP_200_OK)

        context = {
            'result': user_serializer.errors,
            'success': False
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        login_serializer = LoginSerializer(data=request.data)

        if login_serializer.is_valid():
            context = {
                'result': login_serializer.validated_data,
                'success': True
            }
            return Response(context, status=status.HTTP_200_OK)
        context = {
            'result': login_serializer.errors,
            'success': False
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


class RefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_serializer = RefreshTokenSerializer(data=request.data)

        if refresh_serializer.is_valid():
            context = {
                'result': refresh_serializer.validated_data,
                'success': True
            }
            return Response(context, status=status.HTTP_200_OK)
        context = {
            'result': refresh_serializer.errors,
            'success': False
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
