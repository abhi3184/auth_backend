from config.db import conn
from models.index import UserTable
from utils.HashPasswor import verify_password
from schemas.index import UserLogin
from sqlalchemy import select
from fastapi import APIRouter, HTTPException
from repository.index import userLoginRepo

class userloginService:
    @staticmethod
    def login_user(req: UserLogin):
        user = userLoginRepo.user_login(req)

        if not user:
            raise HTTPException(status_code=400, detail="User not found")

        if not verify_password(req.password, user.password):
            raise HTTPException(status_code=400, detail="Incorrect password")
        

        # If success, return some token or user info
        return {"success": True, "user": {"id": user.id, "username": user.username}}
