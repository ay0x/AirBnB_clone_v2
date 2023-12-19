#!/usr/bin/python3

"""
This module provides a class to manage database storage
for the Airbnb clone.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base  # This is the declarative base for our models


class DBStorage:
    """Manages MySQL database storage for the program"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and links to created database
        and existing users
        """
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(os.getenv('HBNB_MYSQL_USER'),
                        os.getenv('HBNB_MYSQL_PWD'),
                        os.getenv('HBNB_MYSQL_HOST', default='localhost'),
                        os.getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True
                )

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current databse session (self.__session) all objects
        depending on the class name (argument cls).

        if cls is None, queries all types of objects.

        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj
        """
        from models import storage
        classes = ["User", "State", "City", "Amenity", "Place", "Review"]

        if cls is None:
            objects = []
            for c in classes:
                objects += list(storage.all(eval(c)).values())
        else:
            objects = list(storage.all(cls).values())

        return {obj.__class__.__name__ + '.' + obj.id: obj for obj in objects}

    def new(self, obj):
        """Add the object to the current database session (self.__session).
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session (self.__session).
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session (self.__session) obj
        if not None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database
        session (self.__session) from the engine (self.__engine).
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
			         expire_on_commit=False))
        self.__session = Session()
