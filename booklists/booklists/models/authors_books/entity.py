# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.mysql.types import YEAR
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AuthorsBook(Base):
    __tablename__ = 'authors_books'

    id = Column(BigInteger, primary_key=True)
    author_id = Column(BigInteger, nullable=False)
    book_id = Column(BigInteger, nullable=False)
    created = Column(DateTime, nullable=False)
