#!/usr/bin/python3
import unittest
import json
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Unit test for the City Class. """

    def test_create_city_instance(self):
        """Tests if an instance can be created in the city class"""
        city = City()
        self.assertIsInstance(city, City)
    def test_city_properties(self):
        """Tests that the initial strings of name and id are empty """
        city = City()
        city.state_id = "KE"
        city.name = "Nairobi"
        self.assertEqual(city.state_id, "KE")
        self.assertEqual(city.name, "Nairobi")

    def test_inheritance_from_base_model(self):
        """Tests if the city class inherits from BaseModel"""
        city =  City()
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_to_dictionnary_method(self):
        """Tests thet the to_dict method returns a dictionary"""
        city = City()
        data_dict = city.to_dict()
        self.assertIsInstance(data_dict, dict)
        self.assertIn('__class__', data_dict)
        self.assertEqual(data_dict['__class__'], 'City')

    def test_str_representation(self):
        """tests that the __str__ method returns the expected string"""
        city = City()
        expected_str = f"[{city.__class__.__name__}] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str)

if __name__ == "__main__":
    unittest.main()

