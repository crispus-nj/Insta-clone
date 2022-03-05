from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Comment, Post
from .forms import PostForm

@login_required(login_url='login')
def home(request):
    post = Post.objects.all().order_by('-date_posted')
    comment = Comment.objects.all()
    context = {'post': post, 'comment': comment}
    return render(request, 'instagram/index.html', context)

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
       image = request.FILES.get('image')
       description = request.POST.get('description')

       post = Post.objects.create(
           user = request.user,
           image = image,
           description = description
       )
       post.save()
    form = PostForm()
    context = {'form': form}
    
    return render(request, 'instagram/create_post.html', context)

