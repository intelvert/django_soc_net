from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('post/new', views.create_post, name='create_post' ),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete', views.delete_post, name='delete_post'),
    #path()
]