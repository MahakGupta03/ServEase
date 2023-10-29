from django.urls import path
from .views import *
urlpatterns = [
    path('', home , name='home'),
    path('register',register,name="register"),
    path('user-login',user_login,name="user-login"),
    path('user-logout',user_logout,name="user-logout"),
]