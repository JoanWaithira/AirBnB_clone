#!/usr/bin/env python3

''' This module defines the base class to be used for this project. '''

from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        ''' Initializes an instance of BaseModel. '''
        current_time = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = current_time
        self.updated_at = current_time
        return

    def __str__(self):
        '''
        Creates the unofficial string representation of a BaseModel instance.
        Format: [<class name>] (<self.id>) <self.__dict__>

        Returns:
            The string representation of the object.
        '''
       return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

   def save(self):
       ''' Updates the updated_at attribute with the current_time. '''
       self.updated_at = datetime.now()
       return
