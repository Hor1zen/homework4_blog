# blogs/views.py
from django.shortcuts import render, redirect, get_object_or_404
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

def edit_post(request, post_id):
    """编辑既有帖子"""
    # 根据 ID 获取帖子，如果找不到这就返回 404
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method != 'POST':
        # 初次请求：使用当前帖子的内容填充表单
        form = BlogPostForm(instance=post)
    else:
        # POST 提交的数据：对数据进行处理
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)