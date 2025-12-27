# blogs/forms.py
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    title = forms.CharField(
        label='文章标题',
        max_length=30
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 15, 'cols': 60, 'placeholder': '文章内容（支持markdown语法）'}),
        label='文章内容',
        max_length=10000
    )
    
    class Meta:
        model = BlogPost
        fields = ['title', 'text']  # 只让用户填标题和内容，时间会自动生成
        labels = {
            'title': '文章标题',
        }