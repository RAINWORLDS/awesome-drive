from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/preview/{filename}")
def preview_file(filename: str):
    path = os.path.join("backend/static", filename)
    if not os.path.exists(path):
        return {"error": "File not found"}
    return FileResponse(path, media_type="image/jpeg")
