from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserAccount
from django.contrib import messages


# Create your views here.

def login_user(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        # print("form data: ", form)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            fullname = form.cleaned_data['fullname']
            password = form.cleaned_data['password']

            user = UserAccount.objects.create_user(
                email = email,
                username = username,
                fullname = fullname,
                password = password
            )
            user.save()
            messages.success(request, 'Account registered successfull. Please check ' + email + ' for the activation link!')
            return redirect('register')

        else: 
            print("The form was not submitted!") 
    form = RegistrationForm()
    context = {"form": form}
    return render(request, 'accounts/register.html', context)