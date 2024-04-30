from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserTest(APITestCase):
    def test_register_user(self):
        data = {
            'email': 'test@gmail.com',
            'password': '12345',
            'date_of_birth': '2000-01-01'
        }
        response = self.client.post(reverse('user_register'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['result']['message'], 'Your account has been created.')

    def test_invalid_date(self):
        existing_email = 'test@gmail.com'
        User.objects.create_user(email=existing_email, password='12345')

        data = {
            'email': existing_email,
            'password': 'testpassword',
            'date_of_birth': '2000-01-01'
        }
        response = self.client.post(reverse('user_register'), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['success'], False)
        self.assertEqual(response.data['result']['message'], 'User with this email already exists.')

    def test_empty_body(self):
        response = self.client.post(reverse('user_register'))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['success'], False)
        self.assertEqual(response.data['result']['email'], ['This field is required.'])
        self.assertEqual(response.data['result']['password'], ['This field is required.'])
        self.assertEqual(response.data['result']['date_of_birth'], ['This field is required.'])


class LoginUserTest(APITestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@gmail.com',
            'password': '12345'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_successful_login(self):
        response = self.client.post(reverse('user_login'), self.user_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], True)
        self.assertIn('access', response.data['result'])
        self.assertIn('refresh', response.data['result'])

    def test_incorrect_login(self):
        invalid_data = {
            'email': 'test@gmail.com',
            'password': 'wrong_password'
        }
        response = self.client.post(reverse('user_login'), invalid_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
