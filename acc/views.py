from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views import generic
from django .views.generic import CreateView 
from django.urls import reverse_lazy
from .forms import  UserForm
from django.contrib import messages
from helper.deco import auth_user_not_to_access





# class RegisterView(generic.CreateView):
#     model = User
#     form_class= UserForm
#     # fields= ("username", "email", "password")
#     template_name = 'acc/register.html'
#     success_url= reverse_lazy('login')


@auth_user_not_to_access
def register_req(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'you success with register')
            return redirect('login')
    form = UserForm()
    return render(request,'acc/register.html',{'form':form})        


@auth_user_not_to_access
def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user= authenticate( username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,f"welcome {username}")
                return redirect('index')
    form=AuthenticationForm()
    return render(request,'acc/login.html',{'form':form})           


def logout_req(request):
    logout(request)
    return redirect('index')     