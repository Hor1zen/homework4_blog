# Blog/urls.py
from django.contrib import admin
from django.urls import path, include  # <-- 记得导入 include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), # 转发给 users 应用
    path('', include('blogs.urls')),   # <-- 新增这一行：把空路径转发给 blogs 应用
]