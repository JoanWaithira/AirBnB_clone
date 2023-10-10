#!/usr/bin/python3
""" This model defines the user class and is inheriting from Base model"""

from models.basemodel import BaseModel

class User(BaseModel):
    """The user class is inheriting from BaseModel"""
    def __init__(*args, **kwargs)
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
