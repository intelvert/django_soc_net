from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login_user'),
    path('logout/', LogoutView.as_view(next_page='feed'), name='logout_user'),
    #path('login_pro/', views.login_pro, name='login_user'),
    path('register/', views.register, name='register'),
    #path(),
]