from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import InvalidAccessToken
from user.serializers import UserRegistrationSerializer, UserLoginSerializer


# User registration view
@extend_schema(tags=["User Model"])
@api_view(['POST'])
def user_registration(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User login view
@extend_schema(tags=["User Model"])
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(username=email, password=password)
            if user:
                # Generate access and refresh tokens for the user
                refresh = RefreshToken.for_user(user)
                data = {
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                    'user_id': user.id,
                }
                return Response(data, status=status.HTTP_200_OK)
            return Response({"message": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# User logout view
@extend_schema(tags=["User Model"])
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    access_token = request.auth
    if access_token:
        access_token = str(access_token)
        if InvalidAccessToken.objects.filter(token=access_token).exists():
            return Response({'error': 'Access token is already blacklisted. Please log in again.'},
                            status=status.HTTP_401_UNAUTHORIZED)
        # Add the access token to the list of blacklisted tokens
        InvalidAccessToken.objects.create(token=access_token)
        return Response({'message': 'Logged Out Successfully'}, status=status.HTTP_200_OK)
    return Response({'error': 'No valid access token found.'}, status=status.HTTP_400_BAD_REQUEST)
