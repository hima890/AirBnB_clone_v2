#!/usr/bin/python3
"""
Script to create tables in the database
"""
from models import storage
from models.base_model import Base

# Import all the models here to ensure they are registered properly
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity

# Create all tables in the database
Base.metadata.create_all(storage._DBStorage__engine)
