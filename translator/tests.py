from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class LanguageTransliteratorTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_text_translation(self):
        data = {'context': 'Привет', 'pattern': 'latin'}
        response = self.client.post('/api/convert_text/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 'Privet')

    
