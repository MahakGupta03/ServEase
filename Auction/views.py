from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

from Services.models import Services
from .models import *

from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def create_bid(request):
    data = Auction.objects.all()
    services = Services.objects.all()
    context = {'data' : data,'services' : services}
    if request.method=='POST':
        user = request.user
        service_name = request.POST.get("service_name")
        description = request.POST.get("description")
        end_date = request.POST.get("end_date")
        end_time = request.POST.get("end_time")

        bid = Auction.objects.create(user = user, service_name = service_name, description=description, end_date=end_date, end_time=end_time, is_closed=False)
        bid.save()
        messages.success(request, "Bid is created successfully")
        return render(request, 'Dashboards/customerprofile.html', context=context)
    else:

        for d in data:
            # print(d.start_date == datetime.now().date())
            
            # print(datetime.strptime(str(datetime.now().time()), "%H:%M:%S") )
            # print(d.end_date == datetime.now().time())
            # print(datetime.now().strftime('%H:%M'))
            # print(d.end_time)
            print(type(d.end_time.strftime('%H:%M')))
        return render(request, 'Accounts/bid_form.html', context=context)
    

def update_bid(request, b_id):  
    if request.user.is_authenticated:
        bid = Auction.objects.get(uid = b_id)
        price_uploaded = AuctionPrice.objects.filter(bid = bid)
        try:
            user = AuctionPrice.objects.get(user = request.user, bid = bid)
        except AuctionPrice.DoesNotExist:
            user = None
        
        context = {'price_uploaded' : price_uploaded, 'bid': bid, 'user': user}
        if bid.end_date <datetime.now().date() or (bid.end_date <= datetime.now().date() and bid.end_time < datetime.now().time()):
            bid.is_closed = True
            bid.save()  
            # context['bid'] = bid
    else:
        return HttpResponse("Not authenticated")
            
    return render(request, 'Accounts/bid_detail.html',context=context)
    
def upload_price(request, bid_id, user_id):
    if request.method=='POST':
        bid = Auction.objects.get(uid=bid_id)
        user = CustomUser.objects.get(uid = user_id)
        price = request.POST.get("price")
        user_bid = AuctionPrice.objects.create(bid = bid, user = user, price = price)
        user_bid.save()
        messages.success(request, "You have successfully uploaded your price.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return HttpResponseRedirect(request.path_info)
        # return HttpResponse("done")

def email_confirmation(request, email):
    # return redirect('user-dashboard' , name = request.user.name)
    user = CustomUser.objects.get(email = email)
    return render(request, 'Dashboards/confirmation.html',{'user': user})

def send_confirmation_mail(request, email):
    subject = "Congratulations"
    message = f"You are confirmed for the job by {request.user.name}"
    email_from =  settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email])
    messages.success(request, "Mail has been sent successfully")
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('user-dashboard' , name = request.user.name)
