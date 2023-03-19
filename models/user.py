#!/usr/bin/python3
""" User model"""

"""import models"""
from os import getenv
import sqlalchemy
import json
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from hashlib import md5
from sqlalchemy.ext.declarative import declarative_base
from models.engine.storage import Serializer
from models import storage, Base
from models.role import Role, UserRole
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired)


class User(Base):
    """Representation of a user """
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password_hash = Column(String(128), nullable=False)
    phone = Column(String(15), nullable=True)
    enabled = Column(TINYINT(4), nullable=False, default=0)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    roles = relationship("Role", secondary='user_roles')
        
    
    def serialize(self):
        """ Serializing the object. """
        s_obj = Serializer.serialize(self)
        del s_obj['password_hash']
        return s_obj
    
    def hash_password(self, password):
        """ Func to hash password using PassLib. """
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        """ Func to verify the hashed password. """
        return pwd_context.verify(password, self.password_hash)
    
    def generate_auth_token(self, expiration = 600):
        s = TimedJSONWebSignatureSerializer('secret', expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = TimedJSONWebSignatureSerializer('secret')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = storage.get(User, data['id'])
        return user
