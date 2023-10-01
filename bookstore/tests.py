from datetime import date

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import User
from .models import Category, Author, Book


class UserAuthenticationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@test.com', password='testpassword')

    def authenticate(self):
        login_payload = {
            'email': 'testuser@test.com',
            'password': 'testpassword',
        }
        login_response = self.client.post(reverse('login-user'), login_payload, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        access_token = login_response.data.get('access_token')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    def test_create_author(self):
        self.authenticate()
        url = reverse('author-list')  # Use 'author-list' URL name
        data = {
            'name': 'John Doe',
            'bio': 'A famous author.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.first().name, 'John Doe')

    def test_create_category(self):
        self.authenticate()
        url = reverse('category-list')  # Use 'category-list' URL name
        data = {
            "name": "Fiction"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().name, 'Fiction')

    def test_create_book(self):
        self.authenticate()
        author = Author.objects.create(name='John Doe', bio='A famous author.')
        category = Category.objects.create(name='Fiction')
        url = reverse('book-list')  # Use 'book-list' URL name
        data = {
            'title': 'Sample Book',
            'author': author.id,
            'published_date': date(2023, 1, 1),
            'isbn': '9781234567890',
            'categories': [category.id],
            'price': 19.99
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.first().title, 'Sample Book')
