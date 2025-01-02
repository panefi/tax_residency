from fastapi import APIRouter, HTTPException, Request
from services.travel_service import get_travel_data, add_travel_entry

travel_router = APIRouter()

@travel_router.get('/data', response_model=dict, status_code=200)
async def travel_data(user_id: str):
    """
    Get travel data
    """
    try:
        return get_travel_data(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@travel_router.post('/entry', response_model=dict, status_code=201)
async def travel_entry(request: Request):
    """
    Add a travel entry
    """
    data = await request.json()
    user_id = data['user_id']
    entry = data['entry']
    try:
        return add_travel_entry(user_id, entry)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 