from fastapi import APIRouter, Depends, HTTPException
from services.user_service import get_user_data, register_user, login_user, update_user_profile
from services.middleware import jwt_middleware
from models.users import UserProfileUpdate

users_router = APIRouter()


@users_router.get('/me', response_model=dict, status_code=200)
async def read_user_data(current_user_id: str = Depends(jwt_middleware)):
    """
    Get current user's data
    """
    try:
        return get_user_data(current_user_id)
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


@users_router.post('/login', response_model=dict, status_code=200)
async def login(user_data: dict):
    """
    Login a user
    """
    try:
        return login_user(user_data)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@users_router.put('/update-profile', response_model=dict, status_code=201)
async def update_profile(profile_data: UserProfileUpdate, current_user_id: str = Depends(jwt_middleware)):
    """
    Update user profile
    """
    try:
        return update_user_profile(current_user_id, profile_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
