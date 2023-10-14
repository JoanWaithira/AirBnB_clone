#!/usr/bin/python3
''' This module initializes the FileStorage instance in the project. '''

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
