import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Unit tests for the State class."""

    def test_create_city_instance(self):
        """Tests if an instance in the city class is created"""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_properties(self):
        """Tests if te initial values are strings"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attributes(self):
        """Checks if the state and name attributes are set correctly"""
        city = City()
        city.state_id = "KE"
        city.name = "Nairobi"
        self.assertEqual(city.state_id, "KE")
        self.assertEqual(city.name, "Nairobi")

    def test_base_model_inheritance(self):
        """Tests if city inherits attributes from base model"""
        city = City()
         self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_to_dictionary_method(self):
        """Tests whether to_dict method returns dictionary representation"""
        city = City()
        data_dict = city.to_dict()
        self.assertIsInstance(data_dict, dict)
        self.assertIn('__class__', data_dict)
        self.assertEqual(data_dict['__class__'], 'City')
        self.assertIn('state_id', data_dict)
        self.assertIn('name', data_dict)

    def test_str_representation(self):
        """Tests whether the str method returns a string"""
        city = City()
        expected_str = f"[{city.__class__.__name__}] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str)

if __name__ == '__main__':
    unittest.main()

