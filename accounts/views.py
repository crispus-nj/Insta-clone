from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserAccount
from django.contrib import messages
from django.template.loader import render_to_string

# account verification
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

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

            message_subject = 'INSTA Clone ACTIVATION LINK'
            current_site = get_current_site(request)
            message = render_to_string(request, 'accounts/verification.html', {
                'user' : user,
                'token' : default_token_generator.make_token(user),
                'domain' : current_site,
                'uid': urlsafe_base64_decode(force_bytes(user.id))
            })

            receipient_email = email
            mail = EmailMessage(message_subject, message ,to=[receipient_email])
            mail.send()
            messages.success(request, 'Account registered successfull. Please check ' + email + ' for the activation link!')
            return redirect('register')

        else: 
            print("The form was not submitted!") 
    form = RegistrationForm()
    context = {"form": form}
    return render(request, 'accounts/register.html', context)