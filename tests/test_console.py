#!/usr/bin/env python3

'''This doc_strlen is to be used to test the console module.'''

import unittest
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
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
