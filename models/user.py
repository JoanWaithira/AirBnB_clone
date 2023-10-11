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
