#!/usr/bin/python3
""" Student model"""

import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.engine.storage import Serializer
from models.internship import Internship
from models import storage, Base


class Student(Base):
    """Representation of a user """
    __tablename__ = 'students'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(String(5), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    course_code = Column(String(10), nullable=False)
    student_id = Column(String(50), nullable=False)
    national_id = Column(String(50), nullable=False)
    address = Column(String(128), nullable=False)
    kin_name = Column(String(50), nullable=False)
    kin_phone = Column(String(50), nullable=False)
    payment_approved = Column(TINYINT(4), nullable=False, default=0)
    internship_applications = relationship("Internship", secondary='internship_applications')
    
    def serialize(self):
        s_obj = Serializer.serialize(self)
        del s_obj['national_id']
        del s_obj['internship_applications']
        return s_obj
