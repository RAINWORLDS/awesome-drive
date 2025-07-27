from fastapi import APIRouter, File, UploadFile, Form, HTTPException
import os
from uuid import uuid4

UPLOAD_DIR = "backend/static/"

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), user_id: int = Form(...)):
    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid4().hex}{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    return {"filename": file.filename, "stored_as": filename, "path": filepath}
