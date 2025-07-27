from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

@router.post("/upload/multiple")
async def upload_multiple(files: list[UploadFile] = File(...)):
    count = 0
    for file in files:
        path = os.path.join("backend/static", file.filename)
        with open(path, "wb") as f:
            f.write(await file.read())
        count += 1
    return {"message": "上传成功", "count": count}
