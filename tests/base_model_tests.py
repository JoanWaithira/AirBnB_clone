import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):

    def test_init_default(self):
        """Testing the default initialisation of Base Model."""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test initialization of BaseModel with keyword arguments."""
        data = {
            'id': 'test_id',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-02T00:00:00',
            'name': 'Test Model'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(model.updated_at, datetime.fromisoformat('2023-01-02T00:00:00'))
        self.assertEqual(model.name, 'Test Model')
    def test_str_representation(self):
        """Test the __str__ method of BaseModel."""
        model = BaseModel(id='test_id', name='Test Model')
        expected_str = "[BaseModel] (test_id) {'id': 'test_id', 'name': 'Test Model'}"
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        """Test the save method of BaseModel."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        model = BaseModel(id='test_id', name='Test Model')
        expected_dict = {
            '__class__': 'BaseModel',
            'id': 'test_id',
            'created_at': model.created_at.isoformat(),
            'updated_at': model.updated_at.isoformat(),
            'name': 'Test Model'
        }
        self.assertEqual(model.to_dict(), expected_dict)
    def test_init_with_invalid_kwargs(self):
        """Test initialization of BaseModel with invalid keyword arguments."""
        data = {
            'invalid_key': 'value',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-02T00:00:00',
            'name': 'Test Model'
        }
        with self.assertRaises(AttributeError):
            model = BaseModel(**data)

    def test_update_created_at(self):
        """Test that updating created_at attribute has no effect."""
        model = BaseModel()
        original_created_at = model.created_at
        model.created_at = datetime(2023, 1, 1)
        self.assertEqual(model.created_at, original_created_at)

if __name__ == '__main__':
    unittest.main()
