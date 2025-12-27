# users/urls.py
from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # 包含默认的身份验证 URL (login, logout等)
    path('', include('django.contrib.auth.urls')),
    # 注册页面 (稍后实现)
    path('register/', views.register, name='register'),
]