from django.contrib import admin
from .models import Auction, AuctionPrice
# Register your models here.
admin.site.register(Auction)
admin.site.register(AuctionPrice)
