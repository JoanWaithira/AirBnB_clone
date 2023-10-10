#!/usr/bin/python3
""" This model defines the user class and is inheriting from Base model"""

from models.basemodel import BaseModel

class User(BaseModel):
    """
    The user class is inheriting from BaseModel

    Args:
    email (str): The email address of the user
    password(str): The password
    first_name (str): The first name of the user
    last_name (str): The last name of the user

    """
    def __init__(*args, **kwargs)
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
