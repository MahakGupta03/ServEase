from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.urls import reverse

from Auction.models import *
from Services.models import Services
from .models import CustomUser
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
# from .forms import CustomUserForm

User = get_user_model()

# Create your views here.

def home(request):
    # fm = CustomUserForm()
    # return HttpResponse("Home page")
    services = Services.objects.all()
    context = {'services' : services}
    return render(request,"Home/home.html",context=context)

def register(request):
    services = Services.objects.all()
    context = {'services' : services}
    try:
        if request.method == 'POST':
            name = request.POST.get("name")
            password = request.POST.get("password")
            phone_number = request.POST.get("phone_number")
            email = request.POST.get("email")
            dob = request.POST.get("dob")
            description = request.POST.get("description")
            id_proof_type = request.POST.get("id_proof_type")
            id_proof_number = request.POST.get("id_proof_number")
            address = request.POST.get("address")    
            state = request.POST.get("state")    
            city = request.POST.get("city")    
            district = request.POST.get("district")    
            # dropdown = request.POST.get("dropdown")
            account_type = request.POST.get("a-type")
            profile = request.FILES.get("profile")
            service_name = request.POST.get("service") if account_type == 'service provider' else None
            service_type = Services.objects.get(service_name=service_name) if service_name else None
            # service_name = request.POST.get("service") 
            # service_type = Services.objects.get(service_name=service_name) 

            # if account_type=='customer':
            #     is_customer = True
            #     is_service_provider = False
            # else:
            #     is_service_provider = True
            #     is_customer = False
            fss = FileSystemStorage()
            file = fss.save(profile.name, profile)
            profile_url = fss.url(file)

            if User.objects.filter(email=email).exists():
                messages.warning(request, "User already exists..")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            # user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name)
            # breakpoint()
            # user = User.objects.create_user(name = name, password=password, phone_number=phone_number, email=email, is_customer = is_customer, is_service_provider=is_service_provider)
            # user = User.objects.create_user(name = name, password=password, phone_number=phone_number, email=email, description=description, id_proof_type = id_proof_type ,id_proof_number=id_proof_number, address=address, 
            #                                 state=state, city=city, district = district , profile_image=profile_url , service_name=service_name , service_type = service_type)
            user = User.objects.create_user(name = name, password=password, phone_number=phone_number, email=email,dob=dob, description=description, id_proof_type = id_proof_type ,id_proof_number=id_proof_number, address=address, 
                                            state=state, city=city, district = district , profile_image=profile_url, service_name=service_name)
            print(account_type)
            # user = User.objects.create_user(name = name, password=password, phone_number=phone_number, email=email, id_proof_type = id_proof_type ,id_proof_number=id_proof_number, address=address, 
            #                                 state=state, city=city, district = district , profile_image=profile_url , service_name=service_name , service_type = service_type)
            if account_type=='customer':
                user.is_customer = True
                # user.service_name = None
                # user.service_type = None
            else:
                user.is_service_provider = True
                user.service_type = service_type
                # user.service_type = Services.objects.get(service_name=service_name)
            print("414")
            user.save()
            
            messages.success(request, "User Registered Successfully..")
            return redirect('home')
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # return render(request, 'login.html')
        
        return render(request,"Accounts/register.html",context=context)
        # return HttpResponse("done")

            # fm = CustomUserForm(request.POST)
            
            # if fm.is_valid():
            #     username = fm.cleaned_data['username']
            #     phone_number = fm.cleaned_data['phone_number']
            #     email = fm.cleaned_data['email']
            #     password = fm.cleaned_data['password']
            #     print(username)
            #     user = User.objects.create_user(username=username,phone_number=phone_number,email=email,password=password)
            #     user.save()
            #     return HttpResponse("done")


    except Exception as e:
        return HttpResponse(e)
    
@csrf_exempt
def user_login(request):
    total_bid = Auction.objects.all()
    try:
        if request.method == 'POST':  
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email = email , password=password)
            if user:
                # -----------Customer Dashboard testing----------------
                login(request,user)
                return redirect('user-dashboard' , name = request.user.name)
                # if request.user.is_customer:
                #     return render(request, 'Dashboards/customerdashboard.html')
                # elif request.user.is_service_provider:
                    
                #     # context = {'bids' : total_bid}
                #     # return render(request, 'Dashboards/service_provider_dashboard.html',{'bids' : total_bid})
                #     return redirect('user-dashboard' , name = request.user.name)
                # else:
                #     users = User.objects.all()
                #     context={'users' : users}
                #     login(request,user)
                #     service = Services.objects.all()
                #     return render(request, 'Services/service.html', {'services':service})

                # -----------Customer Dashboard testing end----------------

                # -----------Before Customer Dashboard testing----------------
                    
                # users = User.objects.all()
                # context={'users' : users}
                # login(request,user)
                # service = Services.objects.all()
                # return render(request, 'Services/service.html', {'services':service})
                    
                 # -----------Before Customer Dashboard testing end----------------
                # return 
                # breakpoint()
                # request.headers['Referer'] = request.headers['Origin']
                # return render(request, 'services.html', {'users' : users})
                
                # return redirect('/')
                # return redirect('Accounts:/',{'users' : users})
                # print(request.META.get('HTTP_REFERER'))
                # return HttpResponseRedirect(reverse('home'))
                # return redirect(reverse('home:/',args=(request)))
            else:
                messages.warning(request, "User not found..")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                # return render(request, 'login.html')
            # if user is not None:
            #     print(user)
            #     return HttpResponse("done")
            # return HttpResponse("Enter valid user")
        else:

            return render(request, 'Dashboards/customerdashboard.html', {'bids' : total_bid})
            
            # users = User.objects.all()
            # return render(request, 'services.html', {'users' : users})

            # messages.warning(request, "User not found..")
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return redirect('/')

            # return render(request, 'login.html')
    except Exception as e:
        return HttpResponse(e)
    

def user_profile(request,name):
    return render(request, 'Dashboards/customerprofile.html')
def user_dashboard(request,name):
    if request.user.is_customer:
        auction_prices = AuctionPrice.objects.all().order_by('price')
        print(auction_prices[0].price)
        return render(request, 'Dashboards/customerdashboard.html', {'auction_prices' : auction_prices})
    elif request.user.is_service_provider:
        total_bid = Auction.objects.all()
        return render(request, 'Dashboards/service_provider_dashboard.html', {'bids' : total_bid})
    
def user_logout(request):
    if request.user:
        logout(request)
    return redirect('/')

def bid_user_profile(request,b_user):
    bid_user = AuctionPrice.objects.filter(user = b_user).first

    return render(request, 'Dashboards/bidcustomerprofile.html',{'bid_user':bid_user})