Ahmed Mujtaba
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from likes.models import Like
from posts.models import Post
from posts.serializers import PostSerializer

class TestPostLikeView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user1', password='password')
        self.post = Post.objects.create(user=self.user, caption='This is a test post')
        self.client.force_login(self.user)

    def test_post_like(self):
        url = reverse('post-like', args=[self.post.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Like.objects.filter(user=self.user, post=self.post).count(), 1)

    def test_post_unlike(self):
        Like.objects.create(user=self.user, post=self.post)
        url = reverse('post-like', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Like.objects.filter(user=self.user, post=self.post).count(), 0)

    def test_post_already_liked(self):
        Like.objects.create(user=self.user, post=self.post)
        url = reverse('post-like', args=[self.post.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TestPostLikesView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user1', password='password')
        self.post = Post.objects.create(user=self.user, caption='This is a test post')
        self.client.force_login(self.user)

    def test_get_post_likes(self):
        Like.objects.create(user=self.user, post=self.post)
        url = reverse('post-likes', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'usernames': [self.user.username]})

class TestUserLikedPostsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user1', password='password')
        self.post1 = Post.objects.create(user=self.user, caption='This is a test post 1')
        self.post2 = Post.objects.create(user=self.user, caption='This is a test post 2')
        Like.objects.create(user=self.user, post=self.post1)
        Like.objects.create(user=self.user, post=self.post2)
        self.client.force_login(self.user)

    def test_get_user_liked_posts(self):
        url = reverse('user-liked-posts')
        response = self.client.get(url)
        serializer = PostSerializer([self.post1, self.post2], many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)