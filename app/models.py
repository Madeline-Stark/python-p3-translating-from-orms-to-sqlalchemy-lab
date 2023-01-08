#!/usr/bin/env python3

from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    # Remember which attributes are required when designing a SQLAlchemy data model: 
    # a __tablename__, 
    __tablename__ = 'dogs'
    # a primary_key, 
    # from the documentation and defining a schema lesson:
    id = Column(Integer, primary_key=True)
    # from the solution:
    #  __table_args__ = (PrimaryKeyConstraint('id'),)

    # id = Column(Integer())
    
    # and one or more Columns
    name = Column(String())
    breed = Column(String())
