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

        doc_strlen = len(HBNBCommand().dict_update.__doc__)
        self.assertGreater(doc_strlen, 0)

    def test_pycodestyle(self):
        '''Checking for pycodestyle 2.8.x compliance.'''
        style = pycodestyle.StyleGuide(quiet=True)
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
            HBNBCommand().onecmd("Draco")
            self.assertEqual("*** Unknown syntax: Draco", c.getvalue().strip())


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

    def test_create(self):
        """
        Check the create functions
        Check first all the edges cases, then the creation of
        instances
        """
        output = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(output, f.getvalue().strip())
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create LesTestCesSuicidaire")
            self.assertEqual(output, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            className = "User." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            className = "Amenity." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            className = "City." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            className = "Place." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, models.storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State Useless text")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, models.storage.all().keys())

    def test_show(self):
        """
        Check the show functions
        Check first all the edges cases, then the creation of
        instances
        """
        output = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(output, f.getvalue().strip())
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NotGoodClasses")
            self.assertEqual(output, f.getvalue().strip())
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(output, f.getvalue().strip())
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel NotGoodID")
            self.assertEqual(output, f.getvalue().strip())

        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("NotGoodClasses.show()")
            self.assertEqual(output, f.getvalue().strip())
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
            self.assertEqual(output, f.getvalue().strip())
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(NotGoodID)")
            self.assertEqual(output, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel " + id)
            className = f"[BaseModel] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel "{id}"')
            className = f"[BaseModel] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({id})")
            className = f"[BaseModel] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + id)
            className = f"[User] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User "{id}"')
            className = f"[User] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({id})")
            className = f"[User] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity " + id)
            className = f"[Amenity] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Amenity "{id}"')
            className = f"[Amenity] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({id})")
            className = f"[Amenity] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City " + id)
            className = f"[City] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show City "{id}"')
            className = f"[City] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({id})")
            className = f"[City] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place " + id)
            className = f"[Place] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Place "{id}"')
            className = f"[Place] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({id})")
            className = f"[Place] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review " + id)
            className = f"[Review] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Review "{id}"')
            className = f"[Review] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({id})")
            className = f"[Review] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State " + id)
            className = f"[State] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show State "{id}"')
            className = f"[State] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({id})")
            className = f"[State] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.      show(     {id}     )")
            className = f"[State] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({id}) Coucou les loulou")
            className = f"[State] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                "show State " + id +
                " Je suis un text inutile show State " + id
            )
            className = f"[State] ({id})"
            self.assertIn(className, f.getvalue().strip())

    def test_destroy(self):
        """
        Test the destroy function
        """
        output = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(output, f.getvalue().strip())
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NotGoodClasses")
            self.assertEqual(output, f.getvalue().strip())
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(output, f.getvalue().strip())
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel NotGoodID")
            self.assertEqual(output, f.getvalue().strip())
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("NotGoodClasses.destroy()")
            self.assertEqual(output, f.getvalue().strip())
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
            self.assertEqual(output, f.getvalue().strip())
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(NotGoodID)")
            self.assertEqual(output, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel " + id)
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Amenity " + id)
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy City " + id)
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Place " + id)
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review " + id)
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State " + id)
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User " + id)
            self.assertEqual(models.storage.all(), {})

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy BaseModel "{id}"')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy Amenity "{id}"')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy City "{id}"')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy Place "{id}"')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy Review "{id}"')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy State "{id}"')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy User "{id}"')
            self.assertEqual(models.storage.all(), {})

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy({id})")
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy({id})")
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy({id})")
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy({id})")
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy({id})")
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy({id})")
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy({id})")
            self.assertEqual(models.storage.all(), {})

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.destroy("{id}")')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Amenity.destroy("{id}")')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'City.destroy("{id}")')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Place.destroy("{id}")')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Review.destroy("{id}")')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'State.destroy("{id}")')
            self.assertEqual(models.storage.all(), {})
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.destroy("{id}")')
            self.assertEqual(models.storage.all(), {})

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            count = f.getvalue().strip()
            self.assertEqual(count, "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Amenity")
            count = f.getvalue().strip()
            self.assertEqual(count, "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count City")
            count = f.getvalue().strip()
            self.assertEqual(count, "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Place")
            count = f.getvalue().strip()
            self.assertEqual(count, "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Review")
            count = f.getvalue().strip()
            self.assertEqual(count, "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            count = f.getvalue().strip()
            self.assertEqual(count, "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            count = f.getvalue().strip()
            self.assertEqual(count, "0")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "3")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {id}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "2")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "3")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {id}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "2")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Amenity")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "3")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Amenity {id}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Amenity")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "2")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count City")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "3")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy City {id}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count City")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "2")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Place")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "3")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Place {id}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Place")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "2")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Review")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "3")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Review {id}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Review")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "2")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "3")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy State {id}")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            countOne = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            countTwo = f.getvalue().strip()
        self.assertEqual(countOne, countTwo)
        self.assertEqual(countOne, "2")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count(blablabla)")
            count = f.getvalue().strip()
        self.assertEqual(count, "2")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State blablabla")
            count = f.getvalue().strip()
        self.assertEqual(count, "2")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Axel")
            count = f.getvalue().strip()
        self.assertEqual(count, "0")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Axel.count()")
            count = f.getvalue().strip()
        self.assertEqual(count, "0")

    def test_update(self):
        """
        Test for update function
        """
        output = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(output, f.getvalue().strip())
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NotAClass")
            self.assertEqual(output, f.getvalue().strip())
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(output, f.getvalue().strip())
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel NotAnId")
            self.assertEqual(output, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        output = "** attribute name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {id}")
            self.assertEqual(output, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update BaseModel "{id}"')
            self.assertEqual(output, f.getvalue().strip())
        output = "** value missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {id} name")
            self.assertEqual(output, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update BaseModel "{id}" name')
            self.assertEqual(output, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'destroy BaseModel "{id}"')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update BaseModel {id} name Betty')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update BaseModel {id} name "Betty"')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update BaseModel {id} id 123')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {id}')
            dictClass = f.getvalue().strip()
        self.assertIn(f"'id': '{id}'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update BaseModel {id} created_at Hier')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {id}')
            dictClass = f.getvalue().strip()
        self.assertNotIn(f"'create_at': 'Hier'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update BaseModel {id} updated_at Demain')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {id}')
            dictClass = f.getvalue().strip()
        self.assertNotIn(f"'updated_at': 'Demain'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Amenity {id} name Betty')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Amenity {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Amenity {id} name "Betty"')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Amenity {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update City {id} name Betty')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show City {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update City {id} name "Betty"')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show City {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Place {id} name Betty')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Place {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Place {id} name "Betty"')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Place {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Review {id} name Betty')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Review {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update Review {id} name "Betty"')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Review {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update State {id} name Betty')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show State {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update State {id} name "Betty"')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show State {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update User {id} name Betty')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update User {id} name "Betty"')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.update({id}, name, Betty)')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.update({id}, name, "Betty")')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Amenity.update({id}, name, Betty)')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Amenity {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Amenity.update({id}, name, "Betty")')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Amenity {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'City.update({id}, name, Betty)')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show City {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'City.update({id}, name, "Betty")')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show City {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'City.update({id}, name, Betty)')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show City {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'City.update({id}, name, "Betty")')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show City {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Place.update({id}, name, Betty)')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Place {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Place.update({id}, name, "Betty")')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Place {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Review.update({id}, name, Betty)')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Review {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Review.update({id}, name, "Betty")')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Review {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'State.update({id}, name, Betty)')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show State {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'State.update({id}, name, "Betty")')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show State {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.update({id}, name, Betty)')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.update({id}, name, "Betty")')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {id}')
            dictClass = f.getvalue().strip()
        self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        command = f'BaseModel.update("{id}", '
        command += '{"name": "Betty"})'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            text = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {id}')
            dictClass = f.getvalue().strip()
            self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        command = f'Amenity.update("{id}", '
        command += '{"name": "Betty"})'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            text = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Amenity {id}')
            dictClass = f.getvalue().strip()
            self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        command = f'City.update("{id}", '
        command += '{"name": "Betty"})'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            text = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show City {id}')
            dictClass = f.getvalue().strip()
            self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        command = f'Place.update("{id}", '
        command += '{"name": "Betty"})'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            text = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Place {id}')
            dictClass = f.getvalue().strip()
            self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        command = f'Review.update("{id}", '
        command += '{"name": "Betty"})'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            text = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Review {id}')
            dictClass = f.getvalue().strip()
            self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        command = f'State.update("{id}", '
        command += '{"name": "Betty"})'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            text = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show State {id}')
            dictClass = f.getvalue().strip()
            self.assertIn("'name': 'Betty'", dictClass)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        command = f'User.update("{id}", '
        command += '{"name": "Betty"})'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            text = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {id}')
            dictClass = f.getvalue().strip()
            self.assertIn("'name': 'Betty'", dictClass)


if __name__ == "__main__":
    unittest.main()
