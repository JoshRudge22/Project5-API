from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Profile
from django.contrib.auth.models import User

class ProfileSearchTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create users and profiles
        self.user1 = User.objects.create_user(username='johndoe', password='password123')
        self.profile1 = Profile.objects.create(
            user=self.user1,
            full_name='John Doe',
            location='New York'
        )

        self.user2 = User.objects.create_user(username='janedoe', password='password123')
        self.profile2 = Profile.objects.create(
            user=self.user2,
            full_name='Jane Doe',
            location='Los Angeles'
        )

        self.user3 = User.objects.create_user(username='jackdoe', password='password123')
        self.profile3 = Profile.objects.create(
            user=self.user3,
            full_name='Jack Doe',
            location='Chicago'
        )

    def test_search_by_username(self):
        response = self.client.get(reverse('profile-list'), {'search': 'johndoe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['user'], 'johndoe')

    def test_search_by_full_name(self):
        response = self.client.get(reverse('profile-list'), {'search': 'Jane Doe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['full_name'], 'Jane Doe')

    def test_search_by_location(self):
        response = self.client.get(reverse('profile-list'), {'search': 'Chicago'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['location'], 'Chicago')

    def test_search_no_results(self):
        response = self.client.get(reverse('profile-list'), {'search': 'Nonexistent'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)

    def test_search_partial_match(self):
        response = self.client.get(reverse('profile-list'), {'search': 'doe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)