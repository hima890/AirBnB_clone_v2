#!/usr/bin/python3
"""
class named city that inharits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class named city that represents a city

    Attributes:
        state_id (string): state id.
        name (string): name of the city

    """

    state_id = ""
    name = ""
