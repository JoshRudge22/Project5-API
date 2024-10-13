from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileModelTests(TestCase):

    def setUp(self):
        # Create user and profile in setup to avoid repeating
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.profile = Profile.objects.get(user=self.user)

    def test_profile_creation(self):
        """Test that a profile is created when a user is created."""
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(self.profile.user, self.user)

    def test_profile_fields(self):
        """Test that profile fields are correctly assigned."""
        self.assertIsInstance(self.profile.full_name, str)
        self.assertIsInstance(self.profile.bio, str)
        self.assertIsInstance(self.profile.location, str)
        self.assertIsInstance(self.profile.profile_image.name, str)

    def test_profile_str_representation(self):
        """Test the string representation of the profile."""
        self.assertEqual(str(self.profile), 'testuser')

    def test_profile_signal_creation(self):
        """Test that profile is automatically created via signal when a user is created."""
        self.assertEqual(Profile.objects.count(), 1)