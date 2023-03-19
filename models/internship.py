#!/usr/bin/python3
""" Internship model"""

import sqlalchemy
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.engine.storage import Serializer
from models import storage, Base
import datetime


class Internship(Base):
    """Representation of an internship """
    __tablename__ = 'internships'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=False)
    industry = Column(String(255), nullable=True)
    job_summary = Column(String(1024), nullable=True)
    location = Column(String(255), nullable=True)
    period_months = Column(Integer, nullable=False, default=0)
    renumeration_in_kes = Column(String(255), nullable=True, default=0)
    start_date = Column(Date, nullable=True)
    added_on = Column(Date, default=datetime.date.today())
    lecturer_id = Column(Integer, nullable=True)
    assigned_student_id = Column(Integer, nullable=True)
    
    def serialize(self):
        s_obj = Serializer.serialize(self)
        return s_obj

class InternshipApplication(Base):
    """Representation of a Internship Application """
    __tablename__ = 'internship_applications'
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'), primary_key=True)
    internship_id = Column(Integer, ForeignKey('internships.id', ondelete='CASCADE'), primary_key=True)
