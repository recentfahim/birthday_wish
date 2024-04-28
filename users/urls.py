from django.urls import path
from .views import RegisterView, LoginView, RefreshTokenView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('refresh-token/', RefreshTokenView.as_view(), name='refresh_token')
]