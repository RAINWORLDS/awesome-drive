from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from backend.database import Base

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    filename = Column(String)
    action = Column(String)
    time = Column(DateTime, default=datetime.utcnow)
