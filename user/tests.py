from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import User  # Adjust this import based on your project structure


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.registration_url = reverse('register-user')
        self.valid_payload = {
            'email': 'test@test.com',
            'password': 'Qwerty123',
        }
        self.invalid_payload = {
            'email': 'invalid_email',
            'password': 'testpassword',
        }

    def test_user_registration_valid_data(self):
        response = self.client.post(self.registration_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_registration_invalid_data(self):
        response = self.client.post(self.registration_url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserLoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('login-user')
        self.user = User.objects.create_user(email='test@example.com', password='testpassword')
        self.valid_payload = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        self.invalid_payload = {
            'email': 'test@example.com',
            'password': 'wrongpassword',
        }

    def test_user_login_valid_credentials(self):
        response = self.client.post(self.login_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login_invalid_credentials(self):
        response = self.client.post(self.login_url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserLogoutTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.logout_url = reverse('logout-user')
        self.user = User.objects.create_user(email='test@example.com', password='testpassword')

    def test_user_logout(self):
        # Log in the user first
        login_payload = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        login_response = self.client.post(reverse('login-user'), login_payload, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)

        # Get the access token from the login response
        access_token = login_response.data.get('access_token')

        # Set the access token in the Authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # Perform the logout
        response = self.client.post(self.logout_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
