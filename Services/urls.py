from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views
from Accounts.views import user_login

urlpatterns = [
    path('services',views.get_services, name='services'),
    path('<id>/users',views.get_user_by_service, name='service-user')
]