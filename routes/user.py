from fastapi import APIRouter
from config.db import conn
from schemas.index import User,UserLogin,EmailOTPRequest,MobileOTPRequest,EmailOTPVerifyRequest,UpdatePasswordReq,VerifyEmailOTPRequest,VerifyMobileOTPRequest
from fastapi import APIRouter, Depends, HTTPException, Body
from schemas.index import UpdateUserRequest

from services.index import userService

user = APIRouter()

@user.get("/users")
async def get_all_users():
    return userService.get_all_users()

@user.get("/users/id/{id}")
async def get_users_By_Id(id:int):   
    return userService.get_user_by_id(id)


@user.get("/users/email")
async def check_user_exist_by_email(email:str):    
    return userService.check_user_exist_by_email(email)
    
@user.put("/updateUser/{user_id}")
async def update_user(user_id: int, payload: UpdateUserRequest):
    result = userService.update_user(user_id, payload)
    return result


@user.delete("/deleteUser/{user_id}")
async def delete_user(user_id: int):
    result = userService.delete_user(user_id)
    return result
