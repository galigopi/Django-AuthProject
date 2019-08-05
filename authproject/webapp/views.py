from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def baseview(request):
    return render(request,'myapp/base.html')
def homeview(request):
    return render(request,'myapp/home.html')
def logoutview(request):
    return render(request, 'myapp/logout.html')
@login_required
def customerview(request):
    return render(request,'myapp/customers.html')

#def registrationview(request):
#    return render(request,'myapp/registration.html')
#def callingview(request):
 #   return HttpResponseRedirect(reverse('login/'))
