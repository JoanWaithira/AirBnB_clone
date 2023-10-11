#!/usr/bin/python3
""" A city class module that inherits from the basemodel class"""

from models.base_model import BaseModel


class City(BaseModel):
    """ A class representing a city"""
    state_id = ""
    name = ""
