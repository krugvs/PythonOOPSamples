# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.mysql.types import YEAR
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Author(Base):
    __tablename__ = 'authors'

    id = Column(BigInteger, primary_key=True)
    firstname = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    year_of_birth = Column(YEAR(4))
