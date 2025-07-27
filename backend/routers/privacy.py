from fastapi import APIRouter, Depends
from backend.database import SessionLocal
from backend.models.file import File

router = APIRouter()

@router.post("/file/privacy")
def set_privacy(filename: str, is_private: bool, db=Depends(SessionLocal)):
    file = db.query(File).filter(File.filename == filename).first()
    if not file:
        return {"error": "文件不存在"}
    file.is_private = is_private
    db.commit()
    return {"message": "隐私设置已更新"}
