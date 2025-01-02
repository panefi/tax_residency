from fastapi import APIRouter, Depends, HTTPException
from services.travel_service import get_travel_data, add_travel_entry
from services.middleware import jwt_middleware

travel_router = APIRouter()

@travel_router.get('/my_travels', response_model=dict, status_code=200)
async def read_travel_data(current_user_id: str = Depends(jwt_middleware)):
    """
    Get current user's travel data
    """
    try:
        return get_travel_data(current_user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@travel_router.post('/add_travel', response_model=dict, status_code=201)
async def create_travel_entry(entry: dict, current_user_id: str = Depends(jwt_middleware)):
    """
    Add a new travel entry for the current user
    """
    try:
        return add_travel_entry(current_user_id, entry)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 