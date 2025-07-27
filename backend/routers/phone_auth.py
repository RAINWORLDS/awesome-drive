from fastapi import APIRouter
from pydantic import BaseModel
from backend.utils.token_gen import generate_code
from backend.services.sms_service import send_sms_code
from backend.database import SessionLocal
from backend.models.user import User

router = APIRouter()

class PhoneRequest(BaseModel):
    phone: str

class PhoneCodeVerify(BaseModel):
    phone: str
    code: str

@router.post("/phone/send")
def send_sms(req: PhoneRequest):
    code = generate_code()
    send_sms_code(req.phone, code)
    return {"message": "验证码已发送"}

@router.post("/phone/verify")
def verify_phone(req: PhoneCodeVerify):
    db = SessionLocal()
    user = db.query(User).filter(User.phone == req.phone).first()
    if not user:
        user = User(phone=req.phone)
        db.add(user)
        db.commit()
    return {"message": "登录成功", "user_id": user.id}
