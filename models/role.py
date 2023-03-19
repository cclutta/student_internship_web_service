#!/usr/bin/python3
""" Roles model"""
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models import Base
from models.engine.storage import Serializer


class Role(Base):
    """Representation of a Role """
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    
    
    def serialize(self):
        """ Serializing the object. """
        s_obj = Serializer.serialize(self)
        del s_obj['id']
        return s_obj
    
class UserRole(Base):
    """Representation of a UserRole """
    __tablename__ = 'user_roles'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True)
