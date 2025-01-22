import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import users_router
from routes.travel import travel_router
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Load allowed origins from environment variable and split into a list
allowed_origins = [origin.strip() for origin in os.getenv("ALLOWED_ORIGINS", "").split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers with versioned URL prefix
app.include_router(users_router, prefix='/api/v1/users')
app.include_router(travel_router, prefix='/api/v1/travel')

if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv('HOST'), port=8000)
