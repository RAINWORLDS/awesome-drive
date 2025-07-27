from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/info/{filename}")
def file_info(filename: str):
    path = os.path.join("backend/static", filename)
    if not os.path.exists(path):
        return {"error": "文件不存在"}
    size = os.path.getsize(path)
    return {"filename": filename, "size": size, "size_kb": size // 1024}
