from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileModelTests(TestCase):
    def test_profile_creation(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'password')
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.username, 'testuser')

    def test_profile_fields(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'password')
        profile = Profile.objects.get(user=user)
        self.assertIsInstance(profile.full_name, str)
        self.assertIsInstance(profile.bio, str)
        self.assertIsInstance(profile.location, str)
        self.assertIsInstance(profile.profile_image.name, str)

    def test_profile_str_representation(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'password')
        profile = Profile.objects.get(user=user)
        self.assertEqual(str(profile), 'testuser')

    def test_profile_signal_creation(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.assertEqual(Profile.objects.count(), 1)