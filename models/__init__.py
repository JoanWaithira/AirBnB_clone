#!/usr/bin/python3
'''This module initializes the FileStorage instance in the project.'''

from models.engine.file_storage import FileStorage

classes = {'BaseModel': 'BaseModel', 'Amenity': 'Amenity', 'State': 'State',
        'Place': 'Place', 'Review': 'Review', 'User': 'User', 'City': 'City'}

storage = FileStorage()
storage.reload()
