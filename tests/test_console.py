#!/usr/bin/env python3

'''This doc_strlen is to be used to test the console module.'''

import pycodestyle
import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestConsoleDocsAndSimpleInputs(unittest.TestCase):
    '''Unittests for the console module.'''

    def test_doc(self):
        '''Tests all code documentation.'''
        # module documentation.
        doc_strlen = len(console.__doc__)
        self.assertGreater(doc_strlen, 0)

        # class documentation.
        doc_strlen = len(HBNBCommand.__doc__)
        self.assertGreater(doc_strlen, 0)

        # function documentations.
        doc_strlen = len(HBNBCommand.do_all.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand.do_EOF.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand.do_quit.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand.do_destroy.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand.do_show.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand.emptyline.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand.do_update.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand.do_count.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand.default.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand.is_float.__doc__)
        self.assertGreater(doc_strlen, 0)

        doc_strlen = len(HBNBCommand.dict_update.__doc__)
        self.assertGreater(doc_strlen, 0)

    def test_pycodestyle(self):
        '''Checking for pycodestyle 2.8.x compliance.'''
        style = pycodestyle.StyleGuide(quiet = True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors found.")

    def test_prompt(self):
        '''Testing the prompt.'''
        self.assertEqual("(hbnb)", HBNBCommand.prompt)

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

    def set_up(self):
        '''Prepare the location for testing.'''
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tear_down(self):
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



if __name__ == "__main__":
    unittest.main()
