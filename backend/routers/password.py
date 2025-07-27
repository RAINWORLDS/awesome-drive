from fastapi import APIRouter, Depends
from pydantic import BaseModel
from backend.database import SessionLocal
from backend.models.user import User

router = APIRouter()

class PasswordSet(BaseModel):
    user_id: int
    password: str

@router.post("/set")
def set_password(data: PasswordSet, db=Depends(SessionLocal)):
    user = db.query(User).filter(User.id == data.user_id).first()
    if not user:
        return {"error": "用户不存在"}
    user.password = data.password
    db.commit()
    return {"message": "密码设置成功"}
