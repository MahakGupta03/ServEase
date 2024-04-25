from django.db import models
from Base.models import BaseModel
from Accounts.models import CustomUser
# Create your models here.

class Auction(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user")
    service_name = models.CharField(max_length = 100)
    description = models.CharField(max_length=500, default=None)
    start_date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)
    end_date = models.DateField()
    end_time = models.TimeField()
    is_closed = models.BooleanField(default=False)

    
class AuctionPrice(BaseModel):
    bid = models.ForeignKey(Auction, on_delete = models.DO_NOTHING, related_name="bid")
    user = models.ForeignKey(CustomUser, on_delete = models.DO_NOTHING, related_name="service_provider")
    price = models.IntegerField() 

    def get_min_bid(self):
        print("ncbxjb")
        total_bid = self.objects.all()
        prices=[]
        for price in total_bid:
            prices.append(price)
        return min(prices)
    
    def get_bid_count(self):
        return self.objects.count()