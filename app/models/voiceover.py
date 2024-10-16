from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Voiceover(Base):
    __tablename__ = "voceovers"

    id = Column(Integer, primary_key=True)
    text = Column(String(256), nullable=False)
    voiceover = Column(String(70), nullable=False)
    voiceover_path = Column(String, unique=True, nullable=False)