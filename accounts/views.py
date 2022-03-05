import os
from django.http import HttpResponse
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
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username'].lower()
            fullname = form.cleaned_data['fullname'].lower()
            password = form.cleaned_data['password']

            user = UserAccount.objects.create_user(
                email = email,
                username = username,
                fullname = fullname,
                password = password
            )

            message_subject = 'INSTA CLONE ACTIVATION LINK'
            current_site = get_current_site(request)
            message = render_to_string('accounts/verification.html', {
                'user' : user,
                'token' : default_token_generator.make_token(user),
                'domain' : current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk))
            })

            echo = os.environ.get('EMAIL_HOST_PASSWORD')
            print(echo)
            user.save()
            receipient_email = email
            send_mail = EmailMessage(message_subject, message ,to=[receipient_email])
            send_mail.send()
            messages.success(request, 'Account registered successfull. Please check [' + receipient_email + '] for the activation link!')
            return redirect('register')

        else: 
            print("The form was not submitted!") 
    form = RegistrationForm()
    context = {"form": form}
    return render(request, 'accounts/register.html', context)

def activate_account(request, uid, token):
    try: 
        uid = urlsafe_base64_decode(uid).decode()
        user = UserAccount._default_manager.get(pk = uid)
    except (ValueError, OverflowError, TypeError, UserAccount.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations your account has been activated!')
        return redirect('login')
    
    else:
        messages.error(request, 'Invalid activation link!')
        return redirect('register')
