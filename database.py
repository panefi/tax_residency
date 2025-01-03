import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

def get_db():
    client = MongoClient(os.getenv('DB_URI'), server_api=ServerApi('1'), tlsCAFile=certifi.where())
    db = client.tax_residency_app
    return db 