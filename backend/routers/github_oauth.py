from fastapi import APIRouter, Request
import requests
from backend.config import settings

router = APIRouter()

@router.get("/login")
def github_login():
    return {
        "redirect": f"https://github.com/login/oauth/authorize?client_id={settings.GITHUB_CLIENT_ID}"
    }

@router.get("/callback")
def github_callback(code: str):
    token_url = "https://github.com/login/oauth/access_token"
    headers = {"Accept": "application/json"}
    data = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "client_secret": settings.GITHUB_CLIENT_SECRET,
        "code": code,
    }
    response = requests.post(token_url, headers=headers, data=data)
    token = response.json().get("access_token")
    user_info = requests.get("https://api.github.com/user", headers={
        "Authorization": f"token {token}"
    }).json()
    return {"github_id": user_info["id"], "username": user_info["login"]}
