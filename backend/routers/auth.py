from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from backend.utils.token_gen import generate_code
from backend.services.email_service import send_email_code
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.user import User

router = APIRouter()

class EmailRequest(BaseModel):
    email: EmailStr

class EmailCodeVerify(BaseModel):
    email: EmailStr
    code: str

@router.post("/email/send")
def send_code_email(req: EmailRequest):
    code = generate_code()
    send_email_code(req.email, code)
    return {"message": "验证码已发送"}

@router.post("/email/verify")
def verify_email(req: EmailCodeVerify, db: Session = Depends(SessionLocal)):
    user = db.query(User).filter(User.email == req.email).first()
    if not user:
        user = User(email=req.email)
        db.add(user)
        db.commit()
    return {"message": "登录成功", "user_id": user.id}
