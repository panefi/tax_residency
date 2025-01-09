from database import get_db
from fastapi.responses import JSONResponse


def get_travel_data(user_id: str):
    db = get_db()
    travel_data = list(db.travel_data.find({'user_id': user_id},
                                           {'_id': 0, 'user_id': 0}))

    return JSONResponse(content={"result": travel_data}, status_code=200)


def add_travel_entry(user_id: str, entry: dict):
    db = get_db()
    db.travel_data.insert_one({
        'user_id': user_id,
        **entry.model_dump()
    })
    return JSONResponse(content={'message': 'Travel entry added successfully'},
                        status_code=201
                        )
