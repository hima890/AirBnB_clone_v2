#!/usr/bin/python3
"""
class named city that inharits from BaseModel
"""
import os
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: foreign key to states.id
        name: input name
    """

    __tablename__ = 'cities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime,
                            nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime,
                            nullable=False, default=datetime.utcnow())
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        state = relationship('State', back_populates='cities')

    else:
        state_id = ""
        name = ""
