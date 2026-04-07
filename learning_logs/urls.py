"""定义learning_logs的URL模式"""
from django.urls import path, re_path
from . import views

app_name = 'learning_logs'#URL请求 
urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('topics/',views.topics,name='topics'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/', views.edit_entry, name='edit_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    ]
