from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from .models import Services
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
User = get_user_model()

# Create your views here.
# def get_services(request,slug):
#     service = Services.objects.all()
#     return render(request,'Services/service.html',{'services':service})

def get_services(request):
    service = Services.objects.all()
    return render(request,'Services/service.html',{'services':service})
def get_user_by_service(request, id):
    try:
        if request.user:
            service_users = User.objects.filter(service_type = id)
            return render(request, 'Services/serviceusers.html', {'service_users' : service_users})
        else:
            messages.warning(request, "Login required")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        return HttpResponse(e)

