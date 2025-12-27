from django.test import TestCase
from django.contrib.auth.models import User
from .models import BlogPost

class BlogPostModelTest(TestCase):
    def setUp(self):
        # 创建一个测试用户
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_string_representation(self):
        """测试模型的字符串表示"""
        post = BlogPost.objects.create(
            title='Test Post',
            text='This is a test post.',
            owner=self.user
        )
        self.assertEqual(str(post), 'Test Post (作者: testuser)')