# blogs/views.py
from django.shortcuts import render
from .models import BlogPost


def index(request):
    """主页：显示所有帖子"""
    # 1. 查询数据库：按 date_added 降序排列 (最新在前)
    posts = BlogPost.objects.order_by('-date_added')

    # 2. 把数据打包成字典
    context = {'posts': posts}

    # 3. 渲染网页
    return render(request, 'blogs/index.html', context)