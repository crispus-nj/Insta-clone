from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Comment, Post

@login_required(login_url='login')
def home(request):
    post = Post.objects.all().order_by('-date_posted')
    # comment = Comment.objects.all()
    context = {'post': post}
    return render(request, 'instagram/index.html', context)

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        description = request.POST.get('description')

        post = Post.objects.create(
            host = request.user,
            image = image,
            description = description
        )
        post.save()
        return redirect('home')
    return render(request, 'instagram/create_post.html')

@login_required(login_url='login')
def post_comment(request, post_id):
    post = Post.objects.get(pk = post_id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        print(comment)
        if comment is None:
            messages.error(request, "Comment can not be empty!")
        else :
            comments = Comment.objects.create(
                user = request.user,
                post = post,
                body = comment
            )
            # comments.save()
            return redirect('home')
    else: 
        print("invalid data")
    return render(request, 'instagram/index.html')

