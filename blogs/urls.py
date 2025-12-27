# blogs/urls.py
from django.urls import path
from . import views

app_name = 'blogs'  # <-- 命名空间，这对以后写链接非常重要

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
]