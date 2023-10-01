from datetime import date

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from bookstore.models import Author, Category, Book
from user.models import User
from .models import Cart, CartItem


class CartAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@test.com', password='testpassword')

    def authenticate(self):
        login_payload = {
            'email': 'testuser@test.com',
            'password': 'testpassword',
        }
        login_response = self.client.post(reverse('login-user'), login_payload, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.token = login_response.data.get('access_token')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def create_data(self):
        self.authenticate()
        self.author = Author.objects.create(name='John Doe', bio='A famous author.')
        self.category = Category.objects.create(name='Fiction')
        self.book = Book.objects.create(
            title='Sample Book',
            author=self.author,
            published_date=date(2023, 1, 1),
            isbn='9781234567890',
            category=[self.category],
            price=19.99
        )
        print(self.book)

    def test_view_cart(self):
        self.authenticate()
        author = Author.objects.create(name='John Doe', bio='A famous author.')
        category = Category.objects.create(name='Fiction')
        book = Book.objects.create(
            title='Sample Book',
            author=author,
            published_date=date(2023, 1, 1),
            isbn='9781234567890',
            price=19.99
        )
        print(book)

        url = reverse('view-cart')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Cart not found')
