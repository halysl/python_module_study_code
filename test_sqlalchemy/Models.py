# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50))
    age = Column('age', Integer)

    def __repr__(self):
        return "<User(id='%s' name='%s' age='%s')>" % (
            self.id, self.name, self.age)


class Role(Base):
    __tablename__ = 'Role'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50))

    def __repr__(self):
        return "<Role(id='%s' name='%s')>" % (self.id, self.name)
