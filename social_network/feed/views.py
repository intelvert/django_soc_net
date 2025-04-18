from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib import messages
from core.utils import is_editable
from .models import Post, Like
from .forms import PostForm
# Create your views here.

def feed(request):
    posts=Post.objects.all().order_by('-created_at') #get all posts on main page
    publishable_posts= [
                            { 
                                'post': post, 
                                'is_editable':is_editable(request.user, post, 1)[0],
                                'liked': post.likes.filter(user=request.user).exists() if request.user.is_authenticated else False,
                            } 
                            for post in posts
                        ] #posts ready for publishing in the feed with "editability" on/off

    return render(request, 'feed/feed.html', {'publishable_posts': publishable_posts})

@login_required
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
    can_edit, error_message = is_editable(request.user, post, 1)
    liked=post.likes.filter(user=request.user).exists() if request.user.is_authenticated else False

    form=None
    if can_edit:
        if request.method=='POST':
            form=PostForm(request.POST, instance=post)
            if form.is_valid():
                post.been_edited=True
                form.save()
                messages.success(request, "Post updated successfully!")
                return redirect('post_detail', post_id=post.id)
        elif request.method=='GET':
            form=PostForm(instance=post)
    else:
        messages.error(request, error_message)
        
    context={'post': post,
             'form': form,
             'is_editable': can_edit,
             'liked': liked}

    return render(request, 'feed/post_detail.html', context=context)

@login_required
def delete_post(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    if post.author!=request.user:
        return HttpResponseForbidden("You have no rights to delete this post.") #add registration, redirect to feed
    if request.method=='POST':
        post.delete()
        return redirect('feed')
    return render(request, 'feed/confirm_delete.html', {'post':post})

@login_required
def edit_post(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    if post.author!=request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    if request.method=='POST':
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post.been_edited=True
            form.save()
            return redirect('post_detail', post_id=post.id)
    elif request.method=='GET':
        form=PostForm(instance=post)
    return render(request, 'feed/edit_post.html', {'form':form, 'post':post})


@login_required
def like_post(request, post_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
        
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    like = Like.objects.filter(user=user, post=post)
    
    if like.exists():
        like.delete()
        return JsonResponse({'liked': False, 'like_count': post.likes.count()})
    else:
        Like.objects.create(user=user, post=post)
        return JsonResponse({'liked': True, 'like_count': post.likes.count()})
