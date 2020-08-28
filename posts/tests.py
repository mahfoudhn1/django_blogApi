from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):
    @classmethod

    def setUpTestData(cls):
        testUser1 = User.objects.create_user(
            username='user1', password='abc123'
        )
        testUser1.save()

        test_post = Post.objects.create(
            author=testUser1,
            title="blog title 2",
            body='blog post two just for testing'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'user1')
        self.assertEqual(title, 'blog title 2')
        self.assertEqual(body, 'blog post two just for testing')