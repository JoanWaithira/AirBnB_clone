#!/usr/bin/python3
"""This module defines the amenity class that inherits from BaseModels"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        Args:
        name (str): The name of the amenity

        """
        super().__init__(*args, **kwargs)
        self.name = ""
