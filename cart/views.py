from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bookstore.models import Book
from django.core.mail import send_mail
from .models import Cart, CartItem
from .serializers import CartSerializer
from .tasks import send_receipt


# View to retrieve the user's cart.
@extend_schema(tags=["Cart Model"])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def view_cart(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    except Cart.DoesNotExist:
        return Response({'detail': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)


# View to add a book to the user's cart.
@extend_schema(tags=["Cart Model"])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_to_cart(request, book_id):
    user = request.user
    print("User:", user)
    cart, created = Cart.objects.get_or_create(user=user)

    try:
        book = Book.objects.get(id=book_id)
        print("Book ID:", book.id, "Title:", book.title)
    except Book.DoesNotExist:
        return Response({'detail': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.quantity = 1
        cart_item.save()

    print("Cart Data:", CartSerializer(cart).data)
    cart.items.add(book.id)

    serializer = CartSerializer(cart)
    return Response(serializer.data)


# View to remove a cart item from the user's cart.
@extend_schema(tags=["Cart Model"])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def remove_from_cart(request, cart_item_id):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        return Response({'detail': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
    except CartItem.DoesNotExist:
        return Response({'detail': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

    cart_item.delete()
    serializer = CartSerializer(cart)
    return Response(serializer.data)


# View to process a payment and send an email receipt.
@extend_schema(tags=["Cart Model"])
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def process_payment(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
        serializer = CartSerializer(cart)

        # Stripe Payment Logic or any Other Payments
        result = send_receipt.delay()

        return Response({'detail': 'Email Sent Successfully'})
    except Cart.DoesNotExist:
        return Response({'detail': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
