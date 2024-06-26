#!/usr/bin/python3
"""
class named place that inharits from BaseModel
"""
import os
import shlex
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Inherits from BaseModel class

     Attributes:
        city_id (string): the City id
        user_id (string): the User id
        name (string): the name of the place.
        description (str): the description of the place
        number_rooms (int):the  number of rooms of the place
        number_bathrooms (int):the  number of bathrooms of the place
        max_guest (int):the  maximum number of guests of the place
        price_by_night (int): the price by night of the place
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
        amenity_ids (list): the list of Amenity ids

    """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.place_id == self.id):
                    result.append(elem)
            return (result)

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, value):
            """ Appends amenity ids to the attribute """
            if type(value) == Amenity and value.id not in self.amenity_ids:
                self.amenity_ids.append(value.id)
