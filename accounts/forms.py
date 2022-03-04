from django import forms
from .models import UserAccount

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs= {
        'class' : 'form-control form-input',
        'placeholder' : 'Password'
    }))
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'class' : 'form-control form-input',
        'placeholder' : 'Confirm Password'
    }))

    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs= {
        'class' : 'form-control form-input',
        'placeholder' : 'Username'
    }))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs= {
        'class' : 'form-control form-input',
        'placeholder' : 'Email'
    }))
    fullname = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs= {
        'class' : 'form-control form-input',
        'placeholder' : 'Fullname'
    }))

    class Meta:
        model = UserAccount
        fields = ['email', 'username', 'fullname']
    def __ini__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['fullname'].widget.attrs['placeholder'] = 'Fullname'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
