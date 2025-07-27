from fastapi import APIRouter
import uuid

router = APIRouter()

share_links = {}

@router.post("/share/{filename}")
def share_file(filename: str):
    share_id = uuid.uuid4().hex
    share_links[share_id] = filename
    return {"share_url": f"/share/{share_id}"}

@router.get("/share/{share_id}")
def access_shared_file(share_id: str):
    filename = share_links.get(share_id)
    if not filename:
        return {"error": "无效链接"}
    return {"filename": filename, "url": f"/files/download/{filename}"}
