from config.db import conn
from models.index import UserTable
from repository.index import userRepos,UserRegistrationRepository

class userService:
    @staticmethod
    def get_all_users():
        result = userRepos.get_all_users()
        return result
    
    @staticmethod
    def get_user_by_id(user_id: int):
        result = conn.execute(UserTable.select().where(UserTable.c.id == user_id)).mappings().all()
        return result

    @staticmethod
    def check_user_exist_by_email(email: str):
        result = UserRegistrationRepository.get_user_by_email(email)
        if result:
            return {"exists": True, "message": "Email already registered"}
        else:
            return {"exists": False, "message": "Email not registered"}
    
    @staticmethod
    def get_user_by_mobile(mobile: str):
        result = UserRegistrationRepository.get_user_by_mobile(mobile)
        return result
    
    @staticmethod
    def update_user(user_id,payload):
        existing = userRepos.get_user_by_Id(user_id)
        if not existing:
            return {"success": False, "message": "User not found"}
        return userRepos.update_user(user_id,payload)
    
    @staticmethod
    def delete_user(user_id: int):
        existing_user = userRepos.get_user_by_Id(user_id)
        if not existing_user:
            return {"success": False, "message": "User not found"}
        
        result = userRepos.delete_user(user_id)
        if result :
            return {"success": True, "message": "User deleted successfully"}
        else:
            return {"success": False, "message": "Failed to delete user"}
