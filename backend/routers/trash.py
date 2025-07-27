from fastapi import APIRouter, Depends
import os, shutil
from backend.database import SessionLocal
from backend.models.trash import Trash

router = APIRouter()

@router.post("/trash/delete/{filename}")
def move_to_trash(filename: str, user_id: int, db=Depends(SessionLocal)):
    src = os.path.join("backend/static", filename)
    dst = os.path.join("backend/trash", filename)
    if os.path.exists(src):
        shutil.move(src, dst)
        db.add(Trash(filename=filename, owner_id=user_id))
        db.commit()
        return {"message": "已移入回收站"}
    return {"error": "文件不存在"}
