from fastapi import APIRouter, File, UploadFile, Form
import os

router = APIRouter()

@router.post("/avatar")
async def upload_avatar(file: UploadFile = File(...), user_id: int = Form(...)):
    ext = os.path.splitext(file.filename)[1]
    filename = f"avatar_{user_id}.jpg"  # 固定为jpg
    filepath = os.path.join("backend/static", filename)

    with open(filepath, "wb") as f:
        f.write(await file.read())

    return {"message": "头像上传成功", "file": filename}
