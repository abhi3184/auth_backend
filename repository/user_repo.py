from config.db import conn
from models.index import UserTable
from schemas.index import User

class userRepos:

    @staticmethod
    def get_all_users():
        result = conn.execute(UserTable.select()).mappings().all()
        return result
    
    @staticmethod
    def get_user_by_Id(id):
        result = conn.execute(UserTable.select().where(UserTable.c.id == id)).mappings().first()
        return result
    
    @staticmethod
    def update_user(user_id,user):
        print('UserData',user)
        result = conn.execute(
            UserTable.update()
            .where(UserTable.c.id == user_id)
            .values(
                username=user.username,
                email=user.email,
                mobile=user.mobile
            )
        )
        conn.commit()
        if result.rowcount == 0: 
            return {"success": False, "message": "User not found"}

        return {"success": True, "message": "User updated successfully"}
    
    @staticmethod
    def delete_user(user_id):
        result = conn.execute(UserTable.delete().where(UserTable.c.id == user_id))
        conn.commit()
        return result
