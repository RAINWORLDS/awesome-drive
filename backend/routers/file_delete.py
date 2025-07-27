from fastapi import APIRouter
import os

router = APIRouter()

@router.delete("/delete/{filename}")
def delete_file(filename: str):
    path = os.path.join("backend/static/", filename)
    if os.path.exists(path):
        os.remove(path)
        return {"message": f"{filename} deleted"}
    return {"error": "File not found"}
