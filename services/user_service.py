from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db


def register_user(data):    
    # Hash the password
    hashed_password = generate_password_hash(data['password'])
    
    # Store the user in the database
    db = get_db()
    db.users.insert_one({
        'username': data['username'],
        'password': hashed_password,
        'full_name': data['full_name']
    })
    return {"result": "User registered successfully"}


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


def add_user(data):
    db = get_db()
    db.users.insert_one(data)
    return {"result": "User added successfully"}