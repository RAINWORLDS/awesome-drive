from fastapi import APIRouter, UploadFile, Form, Depends
import os
from backend.database import SessionLocal
from backend.models.version import FileVersion

router = APIRouter()

@router.post("/upload/versioned")
async def upload_versioned(
    file: UploadFile,
    owner_id: int = Form(...),
    db=Depends(SessionLocal)
):
    filename = file.filename
    versions = db.query(FileVersion).filter(FileVersion.filename == filename).all()
    version_num = len(versions) + 1
    save_path = f"backend/static/v{version_num}_{filename}"
    with open(save_path, "wb") as f:
        f.write(await file.read())
    version = FileVersion(
        filename=filename,
        version=version_num,
        filepath=save_path,
        owner_id=owner_id
    )
    db.add(version)
    db.commit()
    return {"message": f"文件 {filename} 的 v{version_num} 已上传"}
