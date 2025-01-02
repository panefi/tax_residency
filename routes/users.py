from fastapi import APIRouter, HTTPException
from services.user_service import get_user_data, add_user

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

@users_router.post('/', response_model=dict, status_code=201)
async def create_user(user_data: dict):
    """
    Add a new user
    """
    try:
        return add_user(user_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
