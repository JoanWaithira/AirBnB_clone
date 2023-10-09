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
