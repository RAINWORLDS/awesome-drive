from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from backend.database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    filepath = Column(String)
    folder = Column(String, default="root")
    download_count = Column(Integer, default=0)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
