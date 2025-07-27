from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from backend.database import Base

class FileVersion(Base):
    __tablename__ = "file_versions"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    version = Column(Integer)
    filepath = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))
