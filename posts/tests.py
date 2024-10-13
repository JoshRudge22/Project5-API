from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from posts.models import Post
from django.core.files.uploadedfile import SimpleUploadedFile

class TestPostAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password123')
        self.client.force_authenticate(user=self.user)
        # Create some posts for testing
        self.post1 = Post.objects.create(user=self.user, caption='Test post 1')
        self.post2 = Post.objects.create(user=self.user, caption='Test post 2')

    def test_feed_list(self):
        response = self.client.get('/feed/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert based on the number of posts you expect, or just check the response format
        self.assertTrue(isinstance(response.data, list))

    def test_post_create(self):
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        data = {'caption': 'Test post', 'image': image}
        response = self.client.post('/posts/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_list(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)  # At least 2 posts created in setUp()

    def test_post_update(self):
        post = Post.objects.create(user=self.user, caption='Test post', image='test_image.jpg')
        data = {'caption': 'Updated test post'}
        response = self.client.patch(f'/posts/{post.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_post_list(self):
        response = self.client.get('/posts/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert based on user posts created
<<<<<<< Updated upstream
        self.assertGreaterEqual(len(response.data), 2)
=======
<<<<<<< HEAD
        self.assertGreaterEqual(len(response.data), 2)
=======
        self.assertGreaterEqual(len(response.data), 2)
>>>>>>> cc7f036 (updated files)
>>>>>>> Stashed changes
