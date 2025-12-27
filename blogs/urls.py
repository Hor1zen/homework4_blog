# blogs/urls.py
from django.urls import path
from . import views

app_name = 'blogs'  # <-- 命名空间，这对以后写链接非常重要

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    # <int:post_id> 是用来接收文章ID的占位符
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]