from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/tags/auto")
def auto_tag(filename: str):
    tags = []
    keywords = ["report", "photo", "code", "backup", "2024"]
    for key in keywords:
        if key.lower() in filename.lower():
            tags.append(key)
    return {"tags": tags or ["misc"]}
