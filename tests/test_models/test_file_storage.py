import unittest
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for File Storage"""


    def test_create_file_storage_instance(self):
        """ Checks if an instance of the FileStorage class can be created."""
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_file_storage_attributes(self):
        """Checks the default attributes of the FileStorage class."""
        fs = FileStorage()
        self.assertEqual(fs._FileStorage__file_path, "file.json")
        self.assertIsInstance(fs._FileStorage__objects, dict)

    def test_all_method(self):
        """Checks if the all method returns a dictionary."""
        fs = FileStorage()
        all_objects = fs.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        """Checks if the new method correctly stores an object"""
        fs = FileStorage()
        new_obj = BaseModel()
        fs.new(new_obj)
        self.assertIn(f"BaseModel.{new_obj.id}", fs._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
