from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post
from .models import Like

class LikeCreateAPIViewTests(APITestCase):
    def setUp(self):
        self.adam = User.objects.create_user(username='adam', password='pass')
        self.brian = User.objects.create_user(username='brian', password='pass')
        self.post = Post.objects.create(owner=self.adam, title='a title', content='content')
    
    def test_can_like_post(self):
        self.client.login(username='Rudge', password='joshua22')
        response = self.client.post('/likes/', {'post': self.post.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)
    
    def test_cannot_like_post_when_not_logged_in(self):
        response = self.client.post('/likes/', {'post': self.post.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Like.objects.count(), 0)
    
    def test_cannot_like_post_twice(self):
        self.client.login(username='Rudge', password='joshua22')
        response = self.client.post('/likes/', {'post': self.post.id})
        response = self.client.post('/likes/', {'post': self.post.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Like.objects.count(), 1)

    def test_can_view_likes(self):
        self.client.login(username='brian', password='pass')
        Like.objects.create(owner=self.brian, post=self.post)
        response = self.client.get(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['like_count'], 1)

    def test_can_view_who_liked_post(self):
        self.client.login(username='brian', password='pass')
        like = Like.objects.create(owner=self.brian, post=self.post)
        response = self.client.get(f'/posts/{self.post.id}/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['owner'], self.brian.username)