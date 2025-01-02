from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db
from pymongo.errors import DuplicateKeyError


def register_user(data):
    db = get_db()
    
    # Check for duplicate username
    existing_user = db.users.find_one({'username': data['username']})
    if existing_user:
        return {"error": "Username already exists"}
    
    hashed_password = generate_password_hash(data['password'])
    
    try:
        db.users.insert_one({
            'username': data['username'],
            'password': hashed_password,
            'full_name': data['full_name']
        })
        return {"result": "User registered successfully"}
    
    except DuplicateKeyError:
        return {"error": "Username already exists"}


def login_user(data):    
    db = get_db()
    user = db.users.find_one({'username': data['username']})
    
    if user and check_password_hash(user['password'], data['password']):
        return {"result": "Login successful"}
    else:
        return {"result": "Invalid username or password"}


def get_user_data(username):
    db = get_db()
    user_data = list(db.users.find({'username': username}, {'_id': 0, 'password': 0}))
    
    return {"result": user_data}
