#!/usr/bin/env python3

'''This module is to be used to test the console module.'''

import pycodestyle
import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
from console import HBNBCommand
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestConsoleDocsAndSimpleInputs(unittest.TestCase):
    '''Unittests for the console module.'''

    def test_doc(self):
        '''Tests all code documentation.'''
        # module documentation.
        doc_strlen = len(console.__doc__)
        self.assertGreater(doc_strlen, 0)

        # class documentation.
        doc_strlen = len(HBNBCommand().__doc__)
        self.assertGreater(doc_strlen, 0)

        # function documentations.
        doc_strlen = len(HBNBCommand().do_all.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand().do_EOF.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand().do_quit.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand().do_destroy.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand().do_show.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand().emptyline.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand().do_update.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand().do_count.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand().default.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand().is_float.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand().dict_update.__doc__)
        self.assertGreater(doc_strlen, 0)

    def test_pycodestyle(self):
        '''Checking for pycodestyle 2.8.x compliance.'''
        style = pycodestyle.StyleGuide(quiet = True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors found.")

    def test_prompt(self):
        '''Testing the prompt.'''
        self.assertEqual("(hbnb)", HBNBCommand().prompt)

    def test_emptyline(self):
        '''Checking the case of no input.'''
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("")
            self.assertEqual("", c.getvalue().strip())

    def test_unknown_command(self):
        '''Checking the case of unknown command.'''
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("Devoir")
            self.assertEqual("*** Unknown syntax: Devoir", c.getvalue().strip())


class TestHelp(unittest.TestCase):
    '''Test the output of help.'''

    def test_help_create(self):
        '''Test the help output of help for create.'''
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("help create")
            self.assertGreater(len(c.getvalue().strip()), 0)

    def test_help_all(self):
        '''Test the help output of help for all.'''
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("help all")
            self.assertGreater(len(c.getvalue().strip()), 0)

    def test_help_destroy(self):
        '''Test the help output of help for destroy.'''
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("help destroy")
            self.assertGreater(len(c.getvalue().strip()), 0)

    def test_help_show(self):
        '''Test the help output of help for show.'''
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("help show")
            self.assertGreater(len(c.getvalue().strip()), 0)

    def test_help_update(self):
        '''Test the help output of help for update.'''
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("help update")
            self.assertGreater(len(c.getvalue().strip()), 0)

    def test_help_EOF(self):
        '''Test the help output of help for EOF.'''
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("help EOF")
            self.assertGreater(len(c.getvalue().strip()), 0)

    def test_help_count(self):
        '''Test the help output of help for count.'''
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("help count")
            self.assertGreater(len(c.getvalue().strip()), 0)

    def test_help_quit(self):
        '''Test the help output of help for quit.'''
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("help quit")
            self.assertGreater(len(c.getvalue().strip()), 0)


class TestFunctions(unittest.TestCase):
    '''Test all the functions.'''

    def setUp(self):
        '''Prepare the location for testing.'''
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        '''After test cleanup.'''
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        '''Testing the all function.'''

        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("all NotAClass")
            self.assertEqual(output, c.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("create Amenity")
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("create City")
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("create Place")
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("create Review")
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("create State")
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("all")
            instances = c.getvalue().strip()

        all_classes = ["Amenity",
                       "BaseModel",
                       "City",
                       "Place",
                       "Review",
                       "State",
                       "User"]
        for classname in all_classes:
            self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("all Amenity")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "Amenity":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("all BaseModel")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "BaseModel":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("all City")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "City":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("all Place")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "Place":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("all Review")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "Review":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("all State")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "State":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("all User")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "User":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)

        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("Amenity.all()")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "Amenity":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("BaseModel.all()")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "BaseModel":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("City.all()")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "City":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("Place.all()")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "Place":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("Review.all()")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "Review":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("State.all()")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "State":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)
        with patch('sys.stdout', new=StringIO()) as c:
            HBNBCommand().onecmd("User.all()")
            instances = c.getvalue().strip()
        for classname in all_classes:
            if classname != "User":
                self.assertNotIn(classname, instances)
            else:
                self.assertIn(classname, instances)


if __name__ == "__main__":
    unittest.main()
