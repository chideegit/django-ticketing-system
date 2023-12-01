from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .form import * 

User = get_user_model()

def register_customer(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False) # don't save form yet
            var.is_customer = True # change is_customer field for this instance to True 
            var.save() # proceed to save
            messages.success(request, 'Account created. Please log in.')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please chec form errors')
            return redirect('register-customer')
    else:
        form = RegisterUserForm()
        context = {'form':form}
    return render(request, 'accounts/register_customer.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'You are logged in as {user}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Active session ended. Log back in to continue')
    return redirect('login')