from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from core.db_mixins import SerializerMixin
import time

Base = declarative_base()


class Note(Base, SerializerMixin):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    creator = Column(Integer)
    created = Column(Integer, default=int(time.time()))
