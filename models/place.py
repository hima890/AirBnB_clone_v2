#!/usr/bin/python3
"""
Class named Place that inherits from BaseModel
"""
import os
import models
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import (Column, Table, String,
                        Integer, Float, ForeignKey,
                        DateTime)
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of rooms in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night: price for staying in int
        latitude: latitude in float
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = 'places'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False,
                            onupdate=datetime.utcnow)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

        reviews = relationship('Review',
                               back_populates='place',
                               cascade='all, delete, delete-orphan'
                               )
        user = relationship('User', back_populates='places')
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities'
                                 )

    else:
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
        amenity_ids = []

        @property
        def reviews(self):
            """Review getter - return list of filtered reviews."""
            reviews_instances = []
            reviews_dict = models.storage.all('Review')
            for key, value in reviews_dict.items():
                if self.id == value.place_id:
                    reviews_instances.append(value)
            return reviews_instances

        @property
        def amenities(self):
            """Amenity getter - return list of amenity instances."""
            all = []
            for amenity_id in self.amenity_ids:
                all.append(models.storage.get('Amenity', amenity_id))
            return all

        @amenities.setter
        def amenities(self, obj):
            """Setter for amenity list"""
            if isinstance(obj, models.amenity.Amenity):
                self.amenity_ids.append(obj.id)
