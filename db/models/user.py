from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from db.db_setup import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(200), nullable=False)


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    full_text = Column(Text, nullable=True)
    link = Column(URLType, nullable=False)
    post_date = Column(String(100), nullable=False)
    digest = Column(String, nullable=False)
    trend = Column(String, nullable=False)
    feature = Column(Text, nullable=False)
    buh_likes = Column(Integer, default=None, nullable=True)
    buisness_likes = Column(Integer, default=None, nullable=True)


class BuisNews(Base):
    __tablename__ = "buisnews"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    full_text = Column(Text, nullable=True)
    link = Column(URLType, nullable=False)
    digest = Column(String, nullable=False)
    trend = Column(String, nullable=False)


class BukhNews(Base):
    __tablename__ = "bukhnews"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    full_text = Column(Text, nullable=True)
    link = Column(URLType, nullable=False)
    digest = Column(String, nullable=False)
    trend = Column(String, nullable=False)
