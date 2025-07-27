from fastapi import APIRouter
import os

router = APIRouter()

@router.post("/rename")
def rename_file(old_name: str, new_name: str):
    old_path = os.path.join("backend/static", old_name)
    new_path = os.path.join("backend/static", new_name)
    if not os.path.exists(old_path):
        return {"error": "原文件不存在"}
    os.rename(old_path, new_path)
    return {"message": f"{old_name} 重命名为 {new_name}"}
