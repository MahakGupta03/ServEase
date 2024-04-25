# from .models import *

# from django.db.models.signals import pre_save,post_save
# from django.dispatch import receiver
# from datetime import datetime
# @receiver(pre_save, sender=Auction)
# def close_auction(sender, instance, **kwargs):
#     end_date = datetime.strptime(instance.end_date, '%Y-%m-%d').date()
#     end_time = datetime.strptime(instance.end_time, '%H:%M').time()
#     # end_time = instance.end_time.strftime('%H:%M')
#     if (end_time <= datetime.now().time()) and not instance.is_closed:
#         # instance.is_closed = True
#         instance.delete()