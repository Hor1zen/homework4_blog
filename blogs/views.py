# blogs/views.py
from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """主页：显示所有帖子"""
    # 按时间降序排列
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def new_post(request):
    """添加新帖子"""
    if request.method != 'POST':
        # 未提交数据：创建一个空表单
        form = BlogPostForm()
    else:
        # POST 提交的数据：对数据进行处理
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    # 显示空表单或无效表单
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)