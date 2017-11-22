# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.mysql.types import YEAR
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Book(Base):
    __tablename__ = 'books'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(500), nullable=False)

