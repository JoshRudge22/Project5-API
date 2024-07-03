from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from posts.models import Post

class TestPostAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password123')
        self.client.force_authenticate(user=self.user)

    def test_feed_list(self):
        response = self.client.get('/feed/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_post_create(self):
        data = {'caption': 'Test post', 'image': 'test_image.jpg'}
        response = self.client.post('/posts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_list(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_post_update(self):
        post = Post.objects.create(user=self.user, caption='Test post', image='test_image.jpg')
        data = {'caption': 'Updated test post'}
        response = self.client.put(f'/posts/{post.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_post_list(self):
        response = self.client.get('/posts/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4) 
