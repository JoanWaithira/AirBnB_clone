#!/usr/bin/python3

"""This module defines class review that inherits from class BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """The review class inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
