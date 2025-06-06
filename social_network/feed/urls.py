from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url="/feed/", permanent=True), name='redirect-to-feed'),
    path('feed/', views.feed, name='feed'),
    path('post/new', views.create_post, name='create_post' ),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/like', views.like_post, name='like_post'),
    #path(),
]