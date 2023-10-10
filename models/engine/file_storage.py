#!/usr/bin/env python3

'''
This module defines FileStorage which is used to serializes and deserializes
instances to and fro json.
'''

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        '''Initializes new FileStorage instance.'''
        return

    def all(self):
        '''
        Accessor of the class attribute __objects.

        Returns:
            The dictionary __objects.
        '''
        return self.__objects

