from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

# Create your views here.

"""def login_pro(request):
        if request.method=='POST':
            username=request['username']
            password=request['password']
            user=authenticate(request, username, password)
            if user is not None:
                login(request, user)
                return redirect('feed')
            else:
                return redirect('login_user') # error message
        else: # not post request error redirect
            return render(request, 'users/login.html', {})"""

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('feed')
    elif request.method=='GET':
        form=RegisterForm()
    return render(request, 'users/register.html', {"form":form})