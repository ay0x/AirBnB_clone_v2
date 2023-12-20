#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")

    else:
        @property
        def cities(self):
            """Returns the list of `City` instances with `state_id` equals
            to the current `State.id` - the FileStorage relationship between
            State and City"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
