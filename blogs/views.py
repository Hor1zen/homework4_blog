# blogs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # 1. 新增导入
from django.http import Http404                            # 2. 新增导入(后面要用)

from .models import BlogPost
from .forms import BlogPostForm

# index 不需要保护
def index(request):
    # ...保持原样...
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required  # 3. 加锁：只有登录才能访问
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

@login_required  # 4. 加锁
def edit_post(request, post_id):
    """编辑既有帖子"""
    post = get_object_or_404(BlogPost, id=post_id)

    if post.owner != request.user:
        # 以前是 raise Http404，现在改成渲染提示页
        return render(request, 'blogs/not_owner.html')

    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)