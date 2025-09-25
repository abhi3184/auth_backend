# config/jwt_config.py
from datetime import timedelta

SECRET_KEY = "your_secret_key_here"   # keep this safe, maybe in .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # token validity
