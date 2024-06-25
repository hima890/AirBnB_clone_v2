#!/usr/bin/python3
"""
class named amenity that inharits from BaseModel
"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel):
    """An amenity provided by a place/house.

    Attributes:
        name (string): The name of the amenity.
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
