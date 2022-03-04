from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'instagram/index.html')

def login_user(request):
    return render(request, 'instagram/login.html')
def register(request):
    return render(request, 'instagram/register.html')