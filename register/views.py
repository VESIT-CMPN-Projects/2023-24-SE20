from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

def register(response):
    if response.method=="POST":
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/index?username=" + form.cleaned_data['username'])
    else:
        form= RegisterForm()
        
    return render(response, "register/register.html",{"form":form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/index')  # Redirect to the desired page after login
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "register/login.html", {"form": form})