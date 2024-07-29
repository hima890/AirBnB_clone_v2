#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    class_map = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __objects
        """
        if cls is None:
            return self.__objects
        else:
            new_dict = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls) or (
                    isinstance(cls, str) and cls == key.split('.')[0]
                ):
                    new_dict[key] = value
            return new_dict

    def new(self, obj):
        """sets __objects to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value["__class__"]
                if cls_name in self.class_map:
                    self.__objects[key] = self.class_map[cls_name](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """calls reload() for deserializing the JSON file to objects."""
        self.reload()
