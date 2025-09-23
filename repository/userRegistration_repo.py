from config.db import conn
from models.index import UserTable
from schemas.index import User
from sqlalchemy import or_
from sqlalchemy import select
from utils.HashPasswor import hash_password

class UserRegistrationRepository:

    @staticmethod
    def get_user_by_email(email: str):
        return conn.execute(UserTable.select().where(UserTable.c.email == email)).mappings().first()
    
    @staticmethod
    def get_user_by_mobile(mobile: str):
        return conn.execute(UserTable.select().where(UserTable.c.mobile == mobile)).mappings().first()
    
    @staticmethod
    def check_user_exist(user : User):
        result = conn.execute(
            UserTable.select().where(
                or_(
                    UserTable.c.email == user.email,
                    UserTable.c.username == user.username,
                    UserTable.c.mobile == user.mobile
                )
            )
        ).mappings().first()
        return result
    
    @staticmethod
    def post_user(user):
        hashed_pw = hash_password(user.password)

        result = conn.execute(
            UserTable.insert().values(
                username=user.username,
                email=user.email,
                password=hashed_pw,
                mobile=user.mobile,
            )
        )
        conn.commit()

        inserted_id = result.lastrowid
        new_user = conn.execute(
            select(UserTable).where(UserTable.c.id == inserted_id)
        ).mappings().first()

        return {
            "success": True,
            "data": new_user,
            "message": "User registered successfully",
        }


