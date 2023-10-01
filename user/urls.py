from django.urls import path

from user.views import user_login, user_registration, user_logout

urlpatterns = [
    path('register/', user_registration, name='register-user'),
    path('login/', user_login, name='login-user'),
    path('logout/', user_logout, name='logout-user'),
]