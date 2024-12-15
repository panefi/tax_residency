from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
    client = MongoClient(os.getenv('DB_URI'))
    db = client.tax_residency_app
    return db 