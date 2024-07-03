from django.test import TestCase
from.models import Comment, Post
from django.contrib.auth.models import User

class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(user=self.user, caption='Test Post')

    def test_comment_create(self):
        comment = Comment.objects.create(user=self.user, post=self.post, content='This is a test comment')
        self.assertEqual(comment.content, 'This is a test comment')

    def test_comment_str(self):
        comment = Comment.objects.create(user=self.user, post=self.post, content='This is a test comment')
        self.assertEqual(str(comment), f'Comment by {self.user.username} on post {self.post.id}')

    def test_comment_user(self):
        comment = Comment.objects.create(user=self.user, post=self.post, content='This is a test comment')
        self.assertEqual(comment.user, self.user)