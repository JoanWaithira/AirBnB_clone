#!/usr/bin/env python3

'''This module tests the user module.'''

import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    '''Tests for the class user.'''
    def test_create_user_instance(self):
        """Checks the instance can be created"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_properties(self):
        """Checks initial values of strings"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes(self):
        """Checks if attributes can be set and retrierieved"""
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "Sam"
        user.last_name = "Paul"
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "Sam")
        self.assertEqual(user.last_name, "Paul")

    def test_base_model_inheritance(self):
        """Checks inheritance from base model"""
        user = User()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_to_dict_method(self):
        """Checks if to dict method returns a dictionary"""
        user = User()
        data_dict = user.to_dict()
        self.assertIsInstance(data_dict, dict)
        self.assertIn('__class__', data_dict)
        self.assertEqual(data_dict['__class__'], 'User')

    def test_str_representation(self):
        """Checks if a string is returned"""
        user = User()
        expected = f"[{user.__class__.__name__}] ({user.id}) {user.__dict__}"
        self.assertEqual(str(user), expected)


if __name__ == '__main__':
    unittest.main()
