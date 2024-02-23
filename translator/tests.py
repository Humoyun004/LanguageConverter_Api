from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class LanguageTransliteratorTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_text_translation(self):
        data = {'context': 'Привет, мир!', 'pattern': 'latin'}
        response = self.client.post('/api/convert_text/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 'Privet, mir!')

    def test_invalid_pattern(self):
        data = {'context': 'Hello, world!', 'pattern': 'invalid_pattern'}
        response = self.client.post('/api/convert_text/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_invalid_request(self):
        data = {'invalid_field': 'value'}
        response = self.client.post('/api/convert_text/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
