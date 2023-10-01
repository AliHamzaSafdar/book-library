from rest_framework import serializers

from bookstore.serializers import BookSerializer
from cart.models import CartItem, Cart


class CartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'

    def get_items(self, obj):
        cart_items = obj.cartitem_set.all()
        items_list = [{'book_id': item.book.id, 'quantity': item.quantity} for item in cart_items]
        return items_list

from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
