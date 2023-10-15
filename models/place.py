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
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_id = []
        super().__init__(self, *args, **kwargs)
