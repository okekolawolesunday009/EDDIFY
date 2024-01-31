
# such as course ID, title, description, instructor ID (foreign key referencing Users table), etc.
#!/usr/bin/python
""" holds class Place"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


# if models.storage_t == 'db':
#     place_amenity = Table('place_amenity', Base.metadata,
#                           Column('place_id', String(60),
#                                  ForeignKey('places.id', onupdate='CASCADE',
#                                             ondelete='CASCADE'),
#                                  primary_key=True),
#                           Column('amenity_id', String(60),
#                                  ForeignKey('amenities.id', onupdate='CASCADE',
#                                             ondelete='CASCADE'),
#                                  primary_key=True))


class Enrollment(BaseModel, Base):
    """Representation of Enrollment """
    if models.storage_t == 'db':
        __tablename__ = 'enrollents'
        course_id = Column(String(60), ForeignKey('courses.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        course_start_date = Column(DateTime, default=datetime.utcnow)
        course_end_date = Column(DateTime, default=datetime.utcnow)
        review_id = Column(String(60),  ForeignKey('reviews.id'), nullable=False)
        
        # reviews = relationship("Review",
        #                        backref="place",
        #                        cascade="all, delete, delete-orphan")
        # amenities = relationship("Amenity",
        #                          secondary=place_amenity,
        #                          viewonly=False)
    else:
        course_id = ""
        user_id = ""
        title = ""
        course_start_date = ""
        course_end_date = ""
        
        # amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    # if models.storage_t != 'db':
    #     @property
    #     def reviews(self):
    #         """getter attribute returns the list of Review instances"""
    #         from models.review import Review
    #         review_list = []
    #         all_reviews = models.storage.all(Review)
    #         for review in all_reviews.values():
    #             if review.place_id == self.id:
    #                 review_list.append(review)
    #         return review_list

    #     @property
    #     def amenities(self):
    #         """getter attribute returns the list of Amenity instances"""
    #         from models.amenity import Amenity
    #         amenity_list = []
    #         all_amenities = models.storage.all(Amenity)
    #         for amenity in all_amenities.values():
    #             if amenity.place_id == self.id:
    #                 amenity_list.append(amenity)
    #         return amenity_list
