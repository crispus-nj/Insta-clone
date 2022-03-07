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

    class Meta:
        model = UserAccount
        fields = ['email', 'username', 'fullname']
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['fullname'].widget.attrs['placeholder'] = 'Fullname'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-input'
    
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password must match!')
        
class UserForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['fullname', 'username' ,'avatar' ,'bio']