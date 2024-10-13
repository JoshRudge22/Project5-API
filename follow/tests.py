from django.test import TestCase
from django.contrib.auth.models import User
from .models import Follow
from django.urls import reverse


class FollowTestCase(TestCase):
    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_follow_user(self):
        # User1 follows User2
        follow = Follow.objects.create(follower=self.user1, followed=self.user2)
        self.assertEqual(Follow.objects.count(), 1)
        self.assertEqual(follow.follower, self.user1)
        self.assertEqual(follow.followed, self.user2)

    def test_unfollow_user(self):
        # User1 follows User2, then unfollows
        follow = Follow.objects.create(follower=self.user1, followed=self.user2)
        follow.delete()
        self.assertEqual(Follow.objects.count(), 0)

    def test_cannot_follow_self(self):
        # User1 tries to follow themselves
        with self.assertRaises(Exception):
            Follow.objects.create(follower=self.user1, followed=self.user1)

    def test_cannot_follow_twice(self):
        # User1 follows User2 twice
        Follow.objects.create(follower=self.user1, followed=self.user2)
        with self.assertRaises(Exception):
            Follow.objects.create(follower=self.user1, followed=self.user2)

    def test_followers_count(self):
        # Check if the followers/following count is updated correctly
        Follow.objects.create(follower=self.user1, followed=self.user2)
        self.assertEqual(self.user2.followers.count(), 1)
        self.assertEqual(self.user1.following.count(), 1)

class FollowViewTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.client.login(username='user1', password='password')
    
    def test_follow_user_view(self):
        response = self.client.post(reverse('follow'), {'followed_id': self.user2.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Follow.objects.count(), 1)
    
    def test_unfollow_user_view(self):
        Follow.objects.create(follower=self.user1, followed=self.user2)
        response = self.client.post(reverse('unfollow'), {'followed_id': self.user2.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Follow.objects.count(), 0)

    def test_follow_self_view(self):
        response = self.client.post(reverse('follow'), {'followed_id': self.user1.id})
        self.assertEqual(response.status_code, 400)  # Assuming your view returns 400 for invalid follow requests