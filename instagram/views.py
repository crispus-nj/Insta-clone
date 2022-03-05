from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Comment, Post

@login_required(login_url='login')
def home(request):
    post = Post.objects.all()
    comment = Comment.objects.all()
    context = {'post': post, 'comment': comment}
    return render(request, 'instagram/index.html', context)

