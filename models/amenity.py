#!/usr/bin/python3
"""
class named amenity that inharits from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house.

    Attributes:
        name (string): The name of the amenity.
    """

    name = ""
