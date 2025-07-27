from fastapi import APIRouter, Depends
from backend.database import SessionLocal
from backend.models.history import History

router = APIRouter()

@router.get("/user/{user_id}")
def get_history(user_id: int, db=Depends(SessionLocal)):
    records = db.query(History).filter(History.user_id == user_id).all()
    return [
        {"file": h.filename, "action": h.action, "time": h.time.isoformat()}
        for h in records
    ]
