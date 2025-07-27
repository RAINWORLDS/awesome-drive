from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from backend.database import Base

class Trash(Base):
    __tablename__ = "trash"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime, default=datetime.utcnow)
