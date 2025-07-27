from backend.database import SessionLocal
from backend.models.log import Log

def log_action(user_id: int, action: str):
    db = SessionLocal()
    db.add(Log(user_id=user_id, action=action))
    db.commit()
    db.close()
