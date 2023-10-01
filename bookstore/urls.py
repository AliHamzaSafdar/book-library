from django.urls import path
from .views import (
    category_list, category_detail,
    author_list, author_detail,
    book_list, book_detail,
)

urlpatterns = [
    # Categories URLs
    path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),

    # Authors URLs
    path('authors/', author_list, name='author-list'),
    path('authors/<int:pk>/', author_detail, name='author-detail'),

    # Books URLs
    path('books/', book_list, name='book-list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
]
