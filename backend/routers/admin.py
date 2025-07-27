from fastapi import APIRouter, Depends
from backend.database import SessionLocal
from backend.models.user import User
from backend.models.file import File

router = APIRouter()

@router.get("/users")
def get_all_users(db=Depends(SessionLocal)):
    users = db.query(User).all()
    return [{"id": u.id, "email": u.email, "phone": u.phone, "github": u.github_id} for u in users]

@router.get("/files")
def get_all_files(db=Depends(SessionLocal)):
    files = db.query(File).all()
    return [{"filename": f.filename, "owner_id": f.owner_id, "created_at": f.created_at.isoformat()} for f in files]
