#!/usr/bin/python3
"""Defines Test Cases"""


import unittest
from datetime import datetime
import json
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class."""

    def test_create_amenity_instance(self):
        """Tests if an instance of Amenity class"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


    def test_amenity_properties(self):
        """Test if the initial value is an empty string"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_attributes(self):
        """Tests if name is set and retrieved correctly"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_to_dict_method(self):
        """Tests if the to_dict method returns the expected dictionary"""
        amenity = Amenity()
        data_dict = amenity.to_dict()
        self.assertIsInstance(data_dict, dict)
        self.assertIn('__class__', data_dict)
        self.assertEqual(data_dict['__class__'], 'Amenity')

    def test_base_model_inheritance(self):
        """Tests if the class inherits correctly base_model"""
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

    def test_str_representation(self):
        """Test if to str method is executed properly"""
        amenity = Amenity()
        expected_str = f"[{amenity.__class__.__name__}] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(str(amenity), expected_str)

if __name__ == '__main__':
    unittest.main()
