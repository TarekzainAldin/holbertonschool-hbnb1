# tests/test_user.py
import unittest
from models import User

class TestUser(unittest.TestCase):
    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
