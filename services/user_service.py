from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db
from pymongo.errors import DuplicateKeyError
import jwt
import os

SECRET_KEY = os.getenv('SECRET_KEY')

def register_user(data):
    db = get_db()
    
    # Check for duplicate username
    existing_user = db.users.find_one({'username': data['username']})
    if existing_user:
        return {"error": "Username already exists"}
    
    hashed_password = generate_password_hash(data['password'])
    
    try:
        result = db.users.insert_one({
            'username': data['username'],
            'password': hashed_password,
            'full_name': data['full_name']
        })
        user_id = str(result.inserted_id)
        return {"result": "User registered successfully", "user_id": user_id}
    
    except DuplicateKeyError:
        return {"error": "Username already exists"}

def login_user(data):    
    db = get_db()
    user = db.users.find_one({'username': data['username']})
    
    if user and check_password_hash(user['password'], data['password']):
        user_id = str(user['_id'])
        token = jwt.encode({'user_id': user_id}, SECRET_KEY, algorithm='HS256')
        return {"token": token}
    else:
        raise Exception("Invalid username or password")

def get_user_data(username):
    db = get_db()
    user_data = list(db.users.find({'username': username}, {'_id': 0, 'password': 0}))
    
    return {"result": user_data}
