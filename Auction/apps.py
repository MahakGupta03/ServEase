from django.apps import AppConfig


class AuctionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Auction'

    # def ready(self):
    #     import Auction.signals 
