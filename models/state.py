#!/usr/bin/python3
"""
class named state that inharits from BaseModel
"""
import os
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities: relationship between state and city tables.
    """

    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime,
                            nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime,
                            nullable=False, default=datetime.utcnow())
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              back_populates='state',
                              cascade='all, delete, delete-orphan'
                              )

    else:
        name = ""

        @property
        def cities(self):
            """returns list of City instances with state_id equal
            to the current State.id"""
            from models import storage
            cities_instances = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_instances.append(city)
            return cities_instances
