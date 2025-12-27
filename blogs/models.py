# blogs/models.py
from django.db import models
from django.contrib.auth.models import User  # 导入 User 模型

class BlogPost(models.Model):
    """用户发布的博客帖子"""
    title = models.CharField(max_length=30)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # owner 外键关联
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """返回模型的字符串表示"""
        return f"{self.title} (作者: {self.owner.username})"