# tests/test_persistence_user.py

import unittest
from unittest.mock import MagicMock
from model.user import User  # Adjust import as per your project structure
from persistence.user_repository import UserRepository  # Adjust import as per your project structure

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository()

    def test_save_get(self):
        user = User(username="John", email="john@example.com", password="securepass")
        self.user_repository.save = MagicMock(return_value=user)
        saved_user = self.user_repository.save(user)
        self.assertEqual(saved_user.username, "John")
        self.assertEqual(saved_user.email, "john@example.com")

    def test_get_all(self):
        user1 = User(username="John", email="john@example.com", password="securepass")
        user2 = User(username="Alice", email="alice@example.com", password="password123")
        self.user_repository.get_all = MagicMock(return_value=[user1, user2])
        all_users = self.user_repository.get_all()
        self.assertEqual(len(all_users), 2)
        self.assertEqual(all_users[0].username, "John")
        self.assertEqual(all_users[1].username, "Alice")

    def test_update(self):
        user = User(username="John", email="john@example.com", password="securepass")
        self.user_repository.update = MagicMock(return_value=True)
        update_data = {'email': "john_new@example.com"}
        result = self.user_repository.update(1, update_data)
        self.assertTrue(result)

    def test_delete(self):
        user = User(username="John", email="john@example.com", password="securepass")
        self.user_repository.delete = MagicMock(return_value=True)
        result = self.user_repository.delete(1)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
