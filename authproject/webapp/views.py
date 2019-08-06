from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webapp.forms import signupform
from django.http import HttpResponseRedirect
# Create your views here.
def homeview(request):
    return render(request,'myapp/home.html')
def logoutview(request):
    return render(request, 'myapp/logout.html')
@login_required
def customerview(request):
    return render(request,'myapp/customers.html')
def registration_view(request):
    form=signupform()
    if request.method =="Post":
        form.signupform(request.post)
        form.save(commit=True)
        return HttpResponseRedirect('/accounts/login')
    return render(request,"myapp/registration.html",{'form':form})

