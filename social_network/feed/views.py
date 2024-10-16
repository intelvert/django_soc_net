from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
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
    return render(request, 'feed/post_detail.html', {'post':post})

def delete_post(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    if post.author!=request.user:
        return HttpResponseForbidden("You have no rights to delete this post.")
    if request.method=='POST':
        post.delete()
        return redirect('feed')
    return render(request, 'feed/confirm_delete.html', {'post':post})
#def like_post
