#!/usr/bin/python3
"""
init models package
"""
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from models.engine.storage import DBStorage
storage = DBStorage()

storage.reload()

