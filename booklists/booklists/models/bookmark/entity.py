# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.mysql.types import YEAR
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Bookmark(Base):
    __tablename__ = 'bookmarks'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    book_id = Column(BigInteger, nullable=False)
    rating = Column(Integer, server_default=FetchedValue())
    review = Column(Text)
    is_private = Column(Integer, nullable=False, server_default=FetchedValue())
    type = Column(Integer, nullable=False, server_default=FetchedValue())
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)

