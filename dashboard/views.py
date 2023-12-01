from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)
