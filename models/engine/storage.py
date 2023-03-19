#!/usr/bin/python3
"""
Contains the class DBStorage
"""

"""import models"""
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.collections import InstrumentedList


Base = declarative_base()




class DBStorage:
    """MySQL DB storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        SI_MYSQL_USER = getenv('SI_MYSQL_USER')
        SI_MYSQL_PWD = getenv('SI_MYSQL_PWD')
        SI_MYSQL_HOST = getenv('SI_MYSQL_HOST')
        SI_MYSQL_DB = getenv('SI_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(SI_MYSQL_USER,
                                             SI_MYSQL_PWD,
                                             SI_MYSQL_HOST,
                                             SI_MYSQL_DB))



    def all(self, cls=None):
        """query on the current database session"""
        objs = self.__session.query(cls).all()
        return (objs)

    def new(self, obj):
        """add object"""
        self.__session.add(obj)

    def save(self):
        """save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        get object by id
        """
        obj = self.__session.query(cls).get(id)
        return obj



class Serializer(object):
    """ Class to serialize my objects. """
    def serialize(self):
        """return {c: getattr(self, c) for c in inspect(self).attrs.keys()}"""
        serializedObject= {}
        for c in inspect(self).attrs.keys():
            attribute = getattr(self, c)
            if(type(attribute) is InstrumentedList ):
                serializedObject[c]= Serializer.serialize_list(attribute)
            else:
                serializedObject[c]= attribute                
        return serializedObject

    @staticmethod
    def serialize_list(lst):
        return [m.serialize() for m in lst]

