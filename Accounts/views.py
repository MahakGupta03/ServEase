from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.urls import reverse
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
    return render(request,"home.html")

def register(request):
    try:
        if request.method == 'POST':
            name = request.POST.get("name")
            password = request.POST.get("password")
            phone_number = request.POST.get("phone_number")
            email = request.POST.get("email")
            id_proof = request.POST.get("id_proof")
            address = request.POST.get("address")
            # dropdown = request.POST.get("dropdown")
            account_type = request.POST.get("a-type")
            profile = request.FILES.get("profile")
            

            fss = FileSystemStorage()
            file = fss.save(profile.name, profile)
            profile_url = fss.url(file)
            
            print(account_type)
            # user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name)
            
            user = User.objects.create_user(name = name,password=password,phone_number=phone_number,email=email, id_proof=id_proof, address=address , profile_image=profile_url )
            if account_type=='customer':
                user.is_customer = True
            else:
                user.is_service_provider = True
            print("414")
            user.save()
            # return HttpResponse("done ")
            messages.success(request, "User Registered Successfully..")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return render(request, 'login.html')
        
        

        return render(request,"register.html")

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
    try:
        if request.method == 'POST':  
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email = email , password=password)

            if user:
                users = User.objects.all()
                context={'users' : users}
                login(request,user)
                # return 
                # breakpoint()
                # request.headers['Referer'] = request.headers['Origin']
                return render(request, 'services.html', {'users' : users})
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
            
            users = User.objects.all()
            return render(request, 'services.html', {'users' : users})

            # messages.warning(request, "User not found..")
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return redirect('/')

            # return render(request, 'login.html')
    except Exception as e:
        return HttpResponse(e)
    
def user_logout(request):
    if request.user:
        logout(request)
    return redirect('/')