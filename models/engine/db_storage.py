#!/usr/bin/python3

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.course import Course
from models.user import User
from models.review import Review
from models.lesson import Lesson
from models.enrollment import Enrollment
from models.quiz import Quiz
import sqlalchemy

classes = {"BaseModel": BaseModel, "User": User, "Lesson": Lesson, "Course": Course, "Quiz": Quiz, "Enrollment": Enrollment, "Review": Review}

class DBStorage:
    """Interact with MySQL database"""
    __engine = None
    __session = None
    
    def __init__(self):
        """Instantiate a DBStorage object"""
        EDDIFY_MYSQL_USER = getenv('EDDIFY_MYSQL_USER')
        EDDIFY_MYSQL_PWD = getenv('EDDIFY_MYSQL_PWD')
        EDDIFY_MYSQL_HOST = getenv('EDDIFY_MYSQL_HOST')
        EDDIFY_MYSQL_DB = getenv("EDDIFY_MYSQL_DB")
        EDDIFY_ENV = getenv('EDDIFY_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(EDDIFY_MYSQL_USER,
                                             EDDIFY_MYSQL_PWD,
                                             EDDIFY_MYSQL_HOST,
                                             EDDIFY_MYSQL_DB))
		
        if EDDIFY_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
            """query on the current database session"""
            new_dict = {}
            for clss in classes:
                if cls is None or cls is classes[clss] or cls is clss:
                    objs  = self.__session.query(clss)
                    for  obj in objs:
                        key = obj.__class__name__ + '.' + obj.id
                        new_dict[key] =obj
            return (new_dict)
		
    def new(self, obj):
        """add the object to  the current database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database """
        self.__session.commit()
	
    def delete(self, obj=None):
        """delete from the current database session obj if Not none"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """reload data form the  database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method pn the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Return the object based on the class_name and its ID
        or None if not found
        """
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
            
        return None
    def count(self, cls=None):
        """
        count the number of objects inn storage
        """
        all_class = classes.values()
        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

        