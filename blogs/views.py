# blogs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    # 1. 获取搜索关键词
    query = request.GET.get('q')

    # 2. 根据是否有关键词进行筛选，同时关联用户信息以优化查询
    if query:
        posts_list = BlogPost.objects.select_related('owner').filter(title__icontains=query).order_by('-date_added')
    else:
        posts_list = BlogPost.objects.select_related('owner').order_by('-date_added')

    # 3. 分页处理 (每页5篇)
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {'posts': posts, 'query': query}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """添加新帖子"""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            # ==============================
            # 核心修改：关联当前用户
            # ==============================
            new_post = form.save(commit=False) # 先别存进数据库
            new_post.owner = request.user      # 把当前登录用户设为主人
            new_post.save()                    # 现在可以存了
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """编辑既有帖子"""
    post = get_object_or_404(BlogPost, id=post_id)

    # 权限检查：只有文章所有者才能编辑
    if post.owner != request.user:
        return render(request, 'blogs/not_owner.html',
                     {'message': '你不能编辑这篇帖子，因为它的作者不是你。'})

    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

@login_required
def delete_post(request, post_id):
    """删除帖子"""
    post = get_object_or_404(BlogPost, id=post_id)

    # 权限检查：只有文章所有者才能删除
    if post.owner != request.user:
        return render(request, 'blogs/not_owner.html',
                     {'message': '你不能删除这篇帖子，因为它的作者不是你。'})

    if request.method == 'POST':
        post.delete()
        return redirect('blogs:index')

    return redirect('blogs:index')