from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

from ..db_setup import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    category = Column(String(100), nullable=False)
    gender = Column(String(50), nullable=False)

    interaction = relationship("Interaction", back_populates="owner") # связь, узнать по-точнее


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Integer, index=True, nullable=False)
    news_text = Column(Text, nullable=False)
    feature_0 = Column(Text, nullable=False)  # Узнать какой тип данных будет у feature!
    feature_1 = Column(Text, nullable=False)

    interaction = relationship("Interaction", back_populates="news")


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    news_id = Column(Integer, ForeignKey("news.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    reaction = Column(Boolean)  # like/ dislike boolean или нет?

    owner = relationship("User", back_populates="interaction")
    news = relationship("News", back_populates="interaction")


# class Embedding(Base):
#     __tablename__ = "embeddings"
#
#     user_id =Column()
#     feature = Column()
