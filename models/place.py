#!/usr/bin/env python3
"""This module defines the place class that inherits from the base model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ The place inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        Args:
        city_id (str): The ID of the city located
        user_id (str): The ID of the owner
        name (str): The name of the place
        description (str): Short description of the place
        number_rooms (int): The number of rooms
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The maximum number of guests allowed
        price_by_night (int): The price per night
        latitude (float): The coordinates
        longitude (float): The coordinates
        amenity_ids (list): The list of amenity IDs

        """
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
        self.amenity_ids = []
