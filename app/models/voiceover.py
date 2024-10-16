from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Voceover(Base):
    __tablename__ = "voceovers"

    id = Column(Integer, primary_key=True)
    voceover_path = Column(String, unique=True, nullable=False)