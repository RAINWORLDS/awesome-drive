from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from backend.database import SessionLocal
from backend.models.file import File
import os

router = APIRouter()

@router.get("/download/{filename}")
def download_file(filename: str, db=Depends(SessionLocal)):
    file = db.query(File).filter(File.filename == filename).first()
    if file:
        file.download_count += 1
        db.commit()
    path = os.path.join("backend/static", filename)
    if os.path.exists(path):
        return FileResponse(path, filename=filename)
    return {"error": "File not found"}
