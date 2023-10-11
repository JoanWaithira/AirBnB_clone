#!/usr/bin/python3

""" This module defines class State that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """The State class inherits from the BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        Initialising an instance of the State class

        Args: name (str): The name of the state

        """
        super().__init__(*args, **kwargs)
        self.name = ""
