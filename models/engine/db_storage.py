#!/usr/bin/python3
"""Module to create a mysql engine"""

import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import event


class DBStorage:
    """This class creates the engine for a mysql database storage system"""

    all_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate the engine and drop if test database"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.environ['HBNB_MYSQL_USER'],
            os.environ['HBNB_MYSQL_PWD'],
            os.environ['HBNB_MYSQL_HOST'],
            os.environ['HBNB_MYSQL_DB']), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Set the default charset and collation
        event.listen(Base.metadata, 'before_create', self.set_mysql_engine)

    def set_mysql_engine(self, target, connection, **kw):
        """Set the default charset for MySQL tables"""
        if self.__engine.name == 'mysql':
            connection.execute(text(
                'SET SESSION sql_mode = "NO_ENGINE_SUBSTITUTION";')
                               )
            for table in target.tables.values():
                table.kwargs['mysql_charset'] = 'latin1'
                if 'mysql_collate' in table.kwargs:
                    del table.kwargs['mysql_collate']

    def all(self, cls=None):
        """Query all objects for current session based on class name"""
        obj_dict = {}
        if cls:
            if isinstance(cls, str):
                cls = self.all_classes[cls]
            elif cls.__name__ in self.all_classes:
                cls = self.all_classes[cls.__name__]
            else:
                raise KeyError(f"Class {cls} is not recognized.")
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for cls in self.all_classes.values():
                objects.extend(self.__session.query(cls).all())
        for obj in objects:
            key = obj.__class__.__name__ + '.' + obj.id
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """Commit changes to the current databases session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and current database session"""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ call close on private session. """
        self.__session.close()
        self.reload()
