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

    def test_doc(self):
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

