from django.shortcuts import render

# Create your views here.
def login_user(request):
    return render(request, 'accounts/login.html')
def register(request):
    
    return render(request, 'accounts/register.html')