from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db
from pymongo.errors import DuplicateKeyError
import jwt
import os
import datetime
from bson.objectid import ObjectId
from datetime import timedelta

SECRET_KEY = os.getenv('SECRET_KEY')


def register_user(data):
    db = get_db()
    existing_user = db.users.find_one({'username': data['username']})
    if existing_user:
        return {"result": "Username already exists"}

    hashed_password = generate_password_hash(data['password'])

    try:
        result = db.users.insert_one({
            'username': data['username'],
            'password': hashed_password,
            'full_name': data['full_name']
        })
        user_id = str(result.inserted_id)
        expiration = datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
        token = jwt.encode({'user_id': user_id, 'exp': expiration},
                           SECRET_KEY, algorithm='HS256')

        return {"result": "User registered successfully", "token": token}
    except DuplicateKeyError:
        return {"error": "Username already exists"}


def login_user(data):
    db = get_db()
    user = db.users.find_one({'username': data['username']})

    if user and check_password_hash(user['password'], data['password']):
        user_id = str(user['_id'])
        expiration = datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
        token = jwt.encode({'user_id': user_id, 'exp': expiration},
                           SECRET_KEY, algorithm='HS256')
        return {"token": token}
    else:
        raise Exception("Invalid username or password")


def get_user_data(user_id: str):
    db = get_db()
    user_data = list(db.users.find({'_id': ObjectId(user_id)},
                                   {'_id': 0, 'password': 0}))

    return {"result": user_data}


def verify_token(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}


def update_user_profile(user_id, profile_data):
    db = get_db()
    db.users.update_one({'_id': ObjectId(user_id)}, {'$set': profile_data.model_dump()})
    return {"result": "Profile updated successfully"}
