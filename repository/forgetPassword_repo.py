from config.db import conn
from models.index import UserTable
from sqlalchemy import select
from schemas.index import MobileOTPRequest

class ForgotPassRepository:
    @staticmethod
    def get_user_by_email(email: str):
        return conn.execute(UserTable.select().where(UserTable.c.email == email)).mappings().first()

    @staticmethod
    def update_user(user_id: int, data: dict):
        return conn.execute(UserTable.update().where(UserTable.c.id == user_id).values(**data))
    
    @staticmethod
    def get_user_by_mobile(payload):
        print("mobile",payload)
        result = conn.execute(
            select(UserTable).where(UserTable.c.mobile == payload)
            ).mappings().first()
        print("result",result)
        return result
    
    @staticmethod
    def update_password(email, password):
        from utils.HashPasswor import hash_password
        hashed_pw = hash_password(password)
        conn.execute(UserTable.update().where(UserTable.c.email == email).values(password=hashed_pw))
        conn.commit()
        return {"success": True, "message": "Password updated successfully"}
