from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Comment, Post
from .forms import PostForm

@login_required(login_url='login')
def home(request):
    post = Post.objects.all()
    comment = Comment.objects.all()
    context = {'post': post, 'comment': comment}
    return render(request, 'instagram/index.html', context)

def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
    form = PostForm()
    context = {'form': form}
    
    return render(request, 'instagram/create_post.html', context)

