#!/usr/bin/python3

""" This model defines the user class and is inheriting from Base model"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The user class is inheriting from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(args, kwargs)
