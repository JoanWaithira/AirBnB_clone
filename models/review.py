#!/usr/bin/python3

"""This module defines class review that inherits from class BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """The review class inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        Args:
        place_id (str): The ID of the place
        user_id (str): The user ID of the person who has reviewed
        text (str): The review message

        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
