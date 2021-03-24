from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import *
from rest_framework.test import APIClient

# Create your tests here.

User = get_user_model()

class ChirpTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Yom", password="Ola")
        
    def test_chirp_created(self):
        chirp_obj = Chirp.objects.create(content="my first tweet test", user=self.user)
        self.assertEqual(chirp_obj.id, 1)
        self.assertEqual(chirp_obj.user, self.user)
        
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password="password")
        return client
        
    def test_api_login(self):
        client = self.get_client()
        response = client.get("")
        
