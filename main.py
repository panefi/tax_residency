import uvicorn
from fastapi import FastAPI
from routes.users import users_router
from routes.travel import travel_router
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()

# Register routers with versioned URL prefix
app.include_router(users_router, prefix='/api/v1/users')
app.include_router(travel_router, prefix='/api/v1/travel')

if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv('HOST'), port=8000)
