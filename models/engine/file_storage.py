#!/usr/bin/env python3

'''
This module defines FileStorage which is used to serializes and deserializes
instances to and fro json.
'''

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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

    def new(self, obj):
        '''
        Enters obj into the __objects dictionary.

        Format: <obj class name>.id

        Args:
            obj : Object to be stored into the __objects dictionary.
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        self.__objects[key] = obj

    def save(self):
        '''
        Serializes the __objects dictionary into the json file
        (path: __file_path).
        '''
        dictionary = {}
        for key in self.__objects.keys():
            dictionary[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w+", encoding="utf-8") as file:
            json.dump(dictionary, file)

    def reload(self):
        '''
        Deserializes the stored instances from __file_path and reloads them
        as instances.
        '''
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                dictionary = json.load(file)
                for key, value in dictionary.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except Exception:
            pass
