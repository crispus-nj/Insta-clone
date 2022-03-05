from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.

def login_user(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        print("form data: ", form)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            fullname = form.cleaned_data['fullname']
            password = form.cleaned_data['password']

            print(email, username, fullname, password)
        else: 
            print("The form was not submitted!") 
    form = RegistrationForm()
    context = {"form": form}
    return render(request, 'accounts/register.html', context)