from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/search")
def search_file(query: str):
    files = os.listdir("backend/static")
    results = [f for f in files if query.lower() in f.lower()]
    return {"results": results}
