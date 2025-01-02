from flask import request, jsonify, g
import jwt
import os
from dotenv import load_dotenv
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

security = HTTPBearer()

async def jwt_middleware(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = payload.get('user_id')
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def validate_token(token: str) -> bool:
    # Implement your token validation logic
    return True

def get_user_id_from_token(token: str) -> str:
    # Extract and return the user_id from the token
    return "user_id"