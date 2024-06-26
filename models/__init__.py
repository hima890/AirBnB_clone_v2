#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


"""A unique FileStorage/DBStorage instance for all models."""
storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE'
    ) == 'db' else FileStorage()
storage.reload()
