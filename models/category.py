
#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.quiz import Quiz
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """Representation of category"""
    if models.storage_t == "db":
        __tablename__ = 'categorys'
        title = Column(String(128), nullable=False)
        # quiz = relationship("City",
        #                       backref="state",
        #                       cascade="all, delete, delete-orphan")
    else:
        title = ""

    def __init__(self, *args, **kwargs):
        """initializes Lesson"""
        super().__init__(*args, **kwargs)

    # if models.storage_t != "db":
    #     @property
    #     def cities(self):
    #         """getter for list of city instances related to the state"""
    #         city_list = []
    #         all_cities = models.storage.all(City)
    #         for city in all_cities.values():
    #             if city.state_id == self.id:
    #                 city_list.append(city)
    #         return city_list
