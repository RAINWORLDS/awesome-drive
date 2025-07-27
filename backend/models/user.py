from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    github_id = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
