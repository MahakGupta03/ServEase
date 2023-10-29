from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate,login,logout
from .models import CustomUser
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
            dropdown = request.POST.get("dropdown")
            radio = request.POST.get("fav_language")
            print(radio)
            # user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name)
            
            user = User.objects.create_user(name = name,password=password,phone_number=phone_number,email=email, id_proof=id_proof, address=address )
            print("414")
            user.save()
            # return HttpResponse("done ")
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
    
def user_login(request):
    try:
        if request.method == 'POST':  
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email = email , password=password)

            if user:
                login(request,user)
                return redirect('/')
            else:
                return render(request, 'login.html')
            # if user is not None:
            #     print(user)
            #     return HttpResponse("done")
            # return HttpResponse("Enter valid user")
        else:
            return render(request, 'login.html')
    except Exception as e:
        return HttpResponse(e)
    
def user_logout(request):
    if request.user:
        logout(request)
    return redirect('/')