from django.urls import path

from . import views
from .views import view_cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('cart/', view_cart, name='view-cart'),
    path('cart/add/<int:book_id>/', add_to_cart, name='add-to-cart'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove-from-cart'),
    path('process-payment/', views.process_payment, name='process-payment'),
]
