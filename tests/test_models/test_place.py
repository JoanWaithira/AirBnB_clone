import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Unit tests for the Place class."""

    def test_create_place_instance(self):
        """Tests if an instance can be created in the place class"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_properties(self):
        """Tests if the initial values are as required"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)

    def test_base_model_inheritance(self):
        """Tests whether the inheritance from BaseModel takes place"""
        place = Place()
        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict return."""
        place = Place()
        data_dict = place.to_dict()
        self.assertIsInstance(data_dict, dict)
        self.assertIn('__class__', data_dict)
        self.assertEqual(data_dict['__class__'], 'Place')

    def test_str_representation(self):
        """Tests if the __str__ method return."""
        place = Place()
        expected_str = "[{}] ({}) {}".format(
                place.__class__.__name__,
                place.id,
                place.__dict__)
        self.assertEqual(str(place), expected_str)


if __name__ == '__main__':
    unittest.main()
