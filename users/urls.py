"""为应用程序users定义URL模式"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'
urlpatterns = [
    #登录页面
    path('login/', LoginView.as_view(template_name = 'learning_logs/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'learning_logs:index'), name='logout'), 
    path('register/', views.register, name='register'),                                        
]
