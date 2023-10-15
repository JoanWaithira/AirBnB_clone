#!/usr/bin/python3
"""This module defines class review that inherits from class BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """The review class inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(self, *args, **kwargs)
