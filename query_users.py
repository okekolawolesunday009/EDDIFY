#!/usr/bin/python3
"""documentation"""
import sqlalchemy
from sys import argv, exit
from models.base_model import Base
from user import User
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    users = session.query(User).order_by(User.id).all()

    for user in users:
        print("{}: {}".format(user.id, user.user_name))

    # Close the session
    session.close()
