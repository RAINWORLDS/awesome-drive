from fastapi import APIRouter, Depends
from backend.database import SessionLocal
from backend.models.folder import Folder

router = APIRouter()

@router.post("/folder/create")
def create_folder(name: str, owner_id: int, parent_id: int = None, db=Depends(SessionLocal)):
    folder = Folder(name=name, owner_id=owner_id, parent_id=parent_id)
    db.add(folder)
    db.commit()
    return {"message": "文件夹创建成功"}
