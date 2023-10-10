#!/usr/bin/python3
""" This is a module that defines the state class that inherits from the Base Model"""
from model.base_model import BaseModel


class State(BaseModel):
    """The State class inherits from the BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialising an instance of the State"""
        name = ""
