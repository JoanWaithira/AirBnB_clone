#!/usr/bin/python3
"""This module defines the amenity class that inherits from BaseModels"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an amenity."""

    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
