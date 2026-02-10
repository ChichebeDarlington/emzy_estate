from django.shortcuts import render, redirect
from .forms import UserForm 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Account created")
           return redirect('user_estates:login')
        print("FORM ERRORS >>>", form.errors) 
    else:
        form = UserForm()
    return render(request, 'register.html', {'form':form})

def login_view(request):
     if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("post_estates:home")
     else:
        form = AuthenticationForm()
     return render(request, 'login.html', {"form":form})

def logout_view(request):
     if request.method == "POST":
       logout(request)
       return redirect('post_estates:home')  # redirect wherever you want
