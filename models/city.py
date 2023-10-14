#!/usr/bin/python3
""" A city class module that inherits from the basemodel class"""

from models.base_model import BaseModel


class City(BaseModel):
    """ A class representing a city

        Attributes:
     state_id (str): The ID of the state
     name (str): The name of the city.
     """

    state_id = ""
    name = ""
