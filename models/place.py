#!/usr/bin/env python3
"""This module defines the place class that inherits from the base model"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ The place inherits from BaseModel"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
