from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/list")
def list_files():
    directory = "backend/static/"
    files = os.listdir(directory)
    return [{"filename": f, "size": os.path.getsize(os.path.join(directory, f))} for f in files]
