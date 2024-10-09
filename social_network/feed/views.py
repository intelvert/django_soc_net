from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like
from .forms import PostForm
# Create your views here.

def feed(request):
    posts=Post.objects.all().order_by('-created_at') #get all posts on main page
    return render(request, 'feed/feed.html', {'posts':posts})

def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            # save Post without saving to DB, to add author
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('feed')
    else:
        form=PostForm()
    return render(request, 'feed/create_post.html', {'form':form})


def post_detail(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    render(request, 'feed/post_detail.html', {'post':post})

#def delete_post
#def like_post
