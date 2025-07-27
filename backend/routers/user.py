from fastapi import APIRouter, Depends
from backend.database import SessionLocal
from backend.models.user import User
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/me/{user_id}")
def get_user_profile(user_id: int, db: Session = Depends(SessionLocal)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    return {
        "id": user.id,
        "email": user.email,
        "phone": user.phone,
        "github_id": user.github_id
    }
