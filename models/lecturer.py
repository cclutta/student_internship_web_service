#!/usr/bin/python3
""" Lecturer model"""

import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.engine.storage import Serializer

Base = declarative_base()

class Lecturer(Base):
    """Representation of a lec """
    __tablename__ = 'lecturers'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(String(5), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    department = Column(String(50), nullable=False)
    lecturer_id = Column(String(50), nullable=False)
    national_id = Column(String(50), nullable=False)
    address = Column(String(128), nullable=False)
    
    def serialize(self):
        s_obj = Serializer.serialize(self)
        del s_obj['national_id']
        return s_obj
