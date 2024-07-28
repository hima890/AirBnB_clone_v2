#!/usr/bin/python3
"""
class named state that inharits from BaseModel
"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities = relationship between state and city tables.
    """

    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', back_populates='state',
            cascade='all, delete, delete-orphan')

    else:
        name = ""

        @property
        def cities(self):
            """returns list of Cities and some relationships"""
            from models import storage
            cities_instances = []
            cities_dict = storage.all(City)
            for key, value in cities_dict.items():
                if self.id == value.state_id:
                    cities_instances.append(value)
            return (cities_instances)
