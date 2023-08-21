from django.test import TestCase
from django.urls import reverse


class TestMainMenu(TestCase):


    def test_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Log in via K', response.content.decode())



