from fastapi import APIRouter, HTTPException
from services.user_service import get_user_data, register_user

users_router = APIRouter()

@users_router.get('/{username}', response_model=dict, status_code=200)
async def read_users(username: str):
    """
    Get user data
    """
    try:
        return get_user_data(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@users_router.post('/register', response_model=dict, status_code=201)
async def create_user(user_data: dict):
    """
    Register a new user
    """
    try:
        return register_user(user_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
