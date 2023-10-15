#!/usr/bin/env python3

'''This module tests the file_storage module.'''


import json
import os
import sys
import unittest
import pycodestyle
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class EngineStorageDocTest(unittest.TestCase):
    """
    Test the docs of the file engine
    """

    def test_docs(self):
        """
        Check all the doc of the Amenity Class
        """
        # module documentation
        module = len(file_storage.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(FileStorage.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(FileStorage.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(FileStorage.all.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(FileStorage.new.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(FileStorage.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(FileStorage.reload.__doc__)
        self.assertGreater(module_class, 0)

    def test_pycodeStyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )


class TestFileStorage(unittest.TestCase):
    """Test cases for File Storage"""

    def setUp(self):
        '''Prepares the module for the tests.'''
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        '''Cleanup after testing.'''
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_create_file_storage_instance(self):
        """ Checks if an instance of the FileStorage class can be created."""
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_file_storage_attributes(self):
        """Checks the default attributes of the FileStorage class."""
        fs = FileStorage()
        self.assertIn("_FileStorage__objects", fs.__dict__)
        self.assertIsInstance(fs._FileStorage__objects, dict)
        self.assertIn("_FileStorage__file_path", fs.__dict__)
        self.assertIsInstance(fs._FileStorage__file_path, str)
        self.assertEqual(fs._FileStorage__file_path, "file.json")

    def test_all_method(self):
        """Checks if the all method returns a dictionary."""
        fs = FileStorage()
        all_objects = fs.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        """checks if the new method correctly stores an object"""
        newBaseModel = BaseModel()
        newAmenity = Amenity()
        newCity = City()
        newReview = Review()
        newState = State()
        newUser = User()
        for classname in ["BaseModel." + newBaseModel.id,
                          "Amenity." + newAmenity.id,
                          "Place." + newPlace.id,
                          "City." + newCity.id,
                          "Review." + newReview.id,
                          "State." + newState.id,
                          "User." + newUser.id]:
            self.assertIn(classname, models.storage.all().keys())

    def test_check_save(self):
        """Check the saving of new instances into json file."""
        newBaseModel = BaseModel()
        newAmenity = Amenity()
        newPlace = Place()
        newCity = City()
        newReview = Review()
        newState = State()
        newUser = User()
        models.storage.save()
        with open("file.json", 'r') as f:
            buf = json.load(f)
        for classname in ["BaseModel." + newBaseModel.id,
                          "Amenity." + newAmenity.id,
                          "Place." + newPlace.id,
                          "City." + newCity.id,
                          "Review." + newReview.id,
                          "State." + newState.id,
                          "User." + newUser.id]:
            self.assertIn(classname, buf.keys())

    def test_check_relaod(self):
        """Check the reload method creation of new instances."""
        newBaseModel = BaseModel()
        newAmenity = Amenity()
        newPlace = Place()
        newCity = City()
        newReview = Review()
        newState = State()
        newUser = User()
        models.storage.save()
        FileStorage._FileStorage__objects = {}
        models.storage.reload()
        for className in ["BaseModel." + newBaseModel.id,
                          "Amenity." + newAmenity.id,
                          "Place." + newPlace.id,
                          "City." + newCity.id,
                          "Review." + newReview.id,
                          "State." + newState.id,
                          "User." + newUser.id]:
            self.assertIn(className, models.storage.all().keys())

    def test_check_arguments(self):
        '''Checking the Error output if arguments are used.'''
        with self.assertRaises(AttributeError):
            models.storage.new("Coucou")
        with self.assertRaises(TypeError):
            models.storage.save("Coucou")
        with self.assertRaises(TypeError):
            models.storage.all("Coucou")
        with self.assertRaises(TypeError):
            models.storage.reload("Coucou")


if __name__ == "__main__":
    unittest.main()
