from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


# Login user View
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('You Have Logged In!'))
            return redirect('Main')
        else:
            messages.success(request,('There Was An Error While Logging In!'))
            return redirect('login')
    else:    
        return render(request,'accounts/Login_Page.html',{})


# Logout User view
def logout_user(request):
    logout(request)
    messages.success(request,('You Have Been Logged Out!'))
    return redirect('Main')
    
    
# Register user
def register_user(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)           
            login(request,user) 
            messages.success(request,('Registration Successfull!'))
            return redirect('login')
        else:
            form = RegisterUserForm()
    
    return render(request,'accounts/Register_Page.html',{'form' : form}) 
                
            