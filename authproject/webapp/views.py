from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webapp.forms import SignUpForm
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
    form = SignUpForm()
    if request.method =='POST':
        form=SignUpForm(request.POST)
        User=form.save(commit=True)
        User.set_password(User.password)
        User.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,"myapp/registration.html",{'form':form})

