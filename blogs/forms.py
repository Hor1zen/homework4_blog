# blogs/forms.py
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']  # 只让用户填标题和内容，时间会自动生成
        labels = {
            'title': '文章标题',
            'text': '文章内容',
        }