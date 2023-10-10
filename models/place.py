#!/usr/bin/python3
"""This module defines the reviw class that inherits from the BaseModel class"""

class Review(BaseModel):
    """The review class inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """The instances of a review class"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
