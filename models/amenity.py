#!/usr/bin/python3
"""This module defines the amenity class that inherits from BaseModels"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Available amenities."""
    name = ""
