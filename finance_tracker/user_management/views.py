from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():  
            user = form.get_user()  
            login(request, user)  
            next_page = request.GET.get('next', 'finance_dashboard')  
            return redirect(next_page)  
        else:
            messages.error(request, 'Invalid username or password')  
    
    else:
        form = AuthenticationForm()  

    return render(request, 'login.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('home')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')
