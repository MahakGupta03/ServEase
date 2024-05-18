from django.urls import path
from .views import *
urlpatterns = [
    path('', home , name='home'),
    path('register',register,name="register"),
    path('user-login', user_login, name="user-login"),
    path('user-logout',user_logout,name="user-logout"),
    path('<str:name>/profile',user_profile,name="user-profile"),
    path('<str:name>/dashboard',user_dashboard,name="user-dashboard"),
    path('<str:b_user>/bid_user',bid_user_profile,name="bid-user-profile"),
]