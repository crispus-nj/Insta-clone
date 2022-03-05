from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['placeholder'] = 'Description...'
    
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mt-3'
            # self.fields[field].widget.attrs['class'] = 'form-control'
