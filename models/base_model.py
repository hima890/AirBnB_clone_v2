#!/usr/bin/python3
"""
This module contains the BaseModel class.
"""
import datetime
import uuid
import models


class BaseModel:
    """
    This class serves as a base model for other classes.
    It provides attributes and methods common to all models.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        Attributes:
            id (str): A unique identifier generated using UUID.
            created_at (str): A string representation of the
            creation timestamp.
            updated_at (str): A string representation of the
            last update timestamp.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

            # If it's a new instance, add it to the storage
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if "created_at" in kwargs.keys():
                self.created_at = datetime.datetime.strptime(
                    kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f'
                )
            if 'updated_at' in kwargs.keys():
                self.updated_at = datetime.datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                )

    @classmethod
    def from_dict(cls, obj_dict):
        """
        Recreates an instance of BaseModel from a dictionary representation.

        Args:
            obj_dict (dict): Dictionary representing the object.

        Returns:
            BaseModel: An instance of BaseModel.
        """
        # Assuming 'id', 'created_at', and 'updated_at' are present in obj_dict
        return cls(id=obj_dict['id'],
                   created_at=obj_dict['created_at'],
                   updated_at=obj_dict['updated_at'])

    def save(self):
        """
        Updates the 'updated_at' attribute with the current timestamp.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the object to a dictionary.
        Returns:
            dict: A dictionary representation of the object.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """
        Returns a string representation of the object.
        Returns:
            str: A string containing the class name,
            ID, and attributes.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )
