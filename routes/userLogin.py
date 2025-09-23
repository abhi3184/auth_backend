from fastapi import APIRouter
from schemas.index import UserLogin
from services.index import userloginService

authentication = APIRouter()

@authentication.post("/login")
async def login_user(login_user: UserLogin):
    return userloginService.login_user(login_user)
