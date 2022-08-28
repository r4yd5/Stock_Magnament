from django.test import TestCase
from authentication import models
import random
import json
# Create your tests here.

ruta = open(r'json_files/username.json', 'r')

users = json.load(ruta)

username_random = random.choice(users)['username']
email_random = random.choice(users)['username']
password1_random = random.choice(users)['username']
password2_random = password1_random


class UsuarioTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            usename= username_random,
            email= email_random,
            password1= password1_random,
            password2= password2_random,
        )

    def test_user_creation(self):
        self.assertEqual(self.user.is_active, True)
