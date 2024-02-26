from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class TextViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_lat_to_cyr(self):
        data = {'context': "O‘zbekiston", 'pattern': 'cyrillic'}
        response = self.client.post('/api/convert_text/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 'Ўзбeкистoн')

    def test_cyr_to_lat(self):
        data = {'context': 'Ўзбeкистoн', 'pattern': 'latin'}
        response = self.client.post('/api/convert_text/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], "O‘zbekiston")


class FileViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_lat_to_cyr(self):
        test_text = "O‘zbekiston"
        test_file = SimpleUploadedFile("test_file.txt", test_text.encode('utf-8'))
        data = {'file': test_file, 'pattern': 'cyrillic'}
        response = self.client.post('/api/convert_file/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 'Ўзбeкистoн')

    def test_cyr_to_lat(self):
        test_text = "Ўзбeкистoн"
        test_file = SimpleUploadedFile("test_file.txt", test_text.encode('utf-8'))
        data = {'file': test_file, 'pattern': 'latin'}
        response = self.client.post('/api/convert_file/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 'O‘zbekiston')
