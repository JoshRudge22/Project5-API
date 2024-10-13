from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from.models import Contact
from.serializers import ContactSerializer

class ContactModelTestCase(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            number='1234567890',
            message='Hello, this is a test message.'
        )

    def test_contact_str(self):
        self.assertEqual(str(self.contact), 'John Doe')

class ContactSerializerTestCase(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            number='1234567890',
            message='Hello, this is a test message.'
        )
        self.serializer = ContactSerializer(self.contact)

    def test_serializer_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'name', 'email', 'number', 'message'})

    def test_serializer_data(self):
        data = self.serializer.data
        self.assertEqual(data['name'], 'John Doe')
        self.assertEqual(data['email'], 'johndoe@example.com')
        self.assertEqual(data['number'], '1234567890')
        self.assertEqual(data['message'], 'Hello, this is a test message.')

class ContactViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_get_contacts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_contact(self):
        data = {
            'name': 'Jane Doe',
            'email': 'janedoe@example.com',
            'number': '0987654321',
            'message': 'Hello, this is another test message.'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 2)

    def test_post_contact_invalid_data(self):
        data = {
            'name': '',
            'email': 'invalid_email',
            'number': '1234567890123',
            'message': ''
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_get_contacts_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'John Doe')