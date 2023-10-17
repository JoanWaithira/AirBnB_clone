#!/usr/bin/env python3


import unittest
from models import base_model
from models.base_model import BaseModel
from datetime import datetime
import json
import pycodestyle
import os


class TestBaseModel(unittest.TestCase):
    ''' Tests all features of BaseModel class. '''

    def test_doc(self):
        '''
        Check all docs.
        '''
        # module documentation
        module = len(base_model.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(BaseModel.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(BaseModel.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(BaseModel.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(BaseModel.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(BaseModel.to_dict.__doc__)
        self.assertGreater(module_class, 0)

    def test_pycodeStyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def setUp(self):
        """setUp all instance we need"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        self.my_model1 = BaseModel()
        self.my_model2 = BaseModel()
        self.my_model1.name = "My_First_Model"
        self.my_model1.my_number = 89
        self.my_model_json = self.my_model1.to_dict()

    def tearDown(self):
        """tearDown delete all instance"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass
        del self.my_model1
        del self.my_model2
        del self.my_model_json

    def test_idStr(self):
        """test type of id"""
        self.assertEqual(type(self.my_model1.id), str)

    def test_uniqueId(self):
        """test if id is unique"""
        self.assertNotEqual(self.my_model1.id, self.my_model2.id)

    def test_DateTimeCreated(self):
        """test the date time"""
        self.assertEqual(self.my_model1.created_at, self.my_model1.updated_at)
        self.assertNotEqual(self.my_model1.created_at,
                            self.my_model2.created_at)
        self.assertNotEqual(self.my_model1.updated_at,
                            self.my_model2.updated_at)
        self.my_model2.save()
        self.assertNotEqual(self.my_model2.created_at,
                            self.my_model2.updated_at)

    def test_strRepr(self):
        """test the repr of class"""
        strRep = self.my_model1.__str__()
        self.assertIn(f"[BaseModel] ({self.my_model1.id})", strRep)
        self.assertIn(f"'id': '{self.my_model1.id}'", strRep)
        self.assertIn(
            f"'created_at': {repr(self.my_model1.created_at)}", strRep)
        self.assertIn(
            f"'updated_at': {repr(self.my_model1.updated_at)}", strRep)

    def test_to_dict_contains_added_attributes(self):
        self.assertIn("name", self.my_model_json)
        self.assertIn("my_number", self.my_model_json)

    def test_create_base_model_instance(self):
        """This tests that a new basemodel instance is set up"""
        self.model = BaseModel()

    def test_base_model_initialisation(self):
        """Testing the default initialisation of Base Model."""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        return

    def test_base_model_with_arguments(self):
        """Test initialization of BaseModel with keyword arguments."""
        data = {
            'id': 'test_id',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-02T00:00:00',
            'name': 'Test Model'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime.fromisoformat(
            '2023-01-01T00:00:00'))
        self.assertEqual(model.updated_at, datetime.fromisoformat(
            '2023-01-02T00:00:00'))
        self.assertEqual(model.name, 'Test Model')
        return

    def test_str_representation(self):
        """Test the __str__ method of BaseModel."""
        model = BaseModel(id='test_id', name='Test Model')
        expt = "[BaseModel] (test_id) {'id': 'test_id', 'name': 'Test Model'}"
        self.assertEqual(str(model), expt)
        return

    def test_save_method(self):
        """Test the save method of BaseModel."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)
        return

    def test_to_dictionary_method(self):
        """Checks if the to_dict method returns expected dict rep"""
        base_model = BaseModel()
        data_dict = base_model.to_dict()
        self.assertIsInstance(data_dict, dict)
        self.assertIn('__class__', data_dict)
        self.assertIn('id', data_dict)
        self.assertIn('created_at', data_dict)
        self.assertIn('updated_at', data_dict)


if __name__ == '__main__':
    unittest.main()
