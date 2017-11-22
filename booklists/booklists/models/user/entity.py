# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.mysql.types import YEAR
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(400), nullable=False)
    password = Column(String(255), nullable=False)
    active = Column(Integer, nullable=False, server_default=FetchedValue())
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<User(name='%s', email='%s', active='%s')>" % (
                                self.name, self.email, self.active)


