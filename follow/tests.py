from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Follow

class FollowTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='user2', password='pass123')
        self.user3 = User.objects.create_user(username='user3', password='pass123')
        self.client.login(username='user1', password='pass123')

    def test_follow_user(self):
        response = self.client.post('/api/follow/', {'following': self.user2.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follow.objects.count(), 1)
        self.assertEqual(Follow.objects.first().follower, self.user1)
        self.assertEqual(Follow.objects.first().following, self.user2)

    def test_unfollow_user(self):
        Follow.objects.create(follower=self.user1, following=self.user2)
        response = self.client.delete(f'/api/follow/unfollow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Follow.objects.count(), 0)

    def test_get_followers(self):
        Follow.objects.create(follower=self.user2, following=self.user1)
        Follow.objects.create(follower=self.user3, following=self.user1)
        response = self.client.get(f'/api/follow/followers/{self.user1.username}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_following(self):
        Follow.objects.create(follower=self.user1, following=self.user2)
        Follow.objects.create(follower=self.user1, following=self.user3)
        response = self.client.get(f'/api/follow/following/{self.user1.username}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_follower_following_count(self):
        Follow.objects.create(follower=self.user2, following=self.user1)
        Follow.objects.create(follower=self.user1, following=self.user3)
        response = self.client.get(f'/api/follow/counts/{self.user1.username}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['follower_count'], 1)
        self.assertEqual(response.data['following_count'], 1)