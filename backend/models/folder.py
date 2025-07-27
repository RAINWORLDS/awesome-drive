from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base

class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("folders.id"), nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
