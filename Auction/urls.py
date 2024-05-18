from django.urls import path
from .views import *
urlpatterns = [
    path('bid-form', create_bid , name='create_bid'),
    path('<str:b_id>/bid',update_bid, name='update_bid'),
    path('<str:bid_id>/<str:user_id>/price',upload_price, name='upload_price'),
    path('<str:email>/confirmation',email_confirmation, name='email-confirmation'),
    path('<str:email>',send_confirmation_mail, name='send-mail'),
]