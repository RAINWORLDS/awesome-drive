from fastapi import APIRouter
import os
from backend.database import SessionLocal
from backend.models.file import File
from backend.models.user import User

router = APIRouter()

@router.get("/stats")
def system_stats():
    db = SessionLocal()
    file_count = db.query(File).count()
    user_count = db.query(User).count()

    total_size = sum(
        os.path.getsize(os.path.join("backend/static", f))
        for f in os.listdir("backend/static")
        if os.path.isfile(os.path.join("backend/static", f))
    )

    return {
        "用户数": user_count,
        "文件数": file_count,
        "总容量（MB）": round(total_size / 1024 / 1024, 2)
    }
