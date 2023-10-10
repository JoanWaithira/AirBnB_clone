import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import pycodestyle


class TestBaseModel(unittest.TestCase):
    ''' Tests all features of BaseModel class. '''
    def test_pycodestyle(self):
        '''Tests if the base_model conforms to pycodestyle.'''
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "Non compliance detected.")
        return

    def test_init_default(self):
        """Testing the default initialisation of Base Model."""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        return

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
        return

    def test_str_representation(self):
        """Test the __str__ method of BaseModel."""
        model = BaseModel(id='test_id', name='Test Model')
        expected_str = "[BaseModel] (test_id) {'id': 'test_id', 'name': 'Test Model'}"
        self.assertEqual(str(model), expected_str)
        return

    def test_save_method(self):
        """Test the save method of BaseModel."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)
        return

if __name__ == '__main__':
    unittest.main()
