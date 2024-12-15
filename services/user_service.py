from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db
from flask import jsonify


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
    
    return jsonify({'message': 'User registered successfully'}), 201


def login_user(data):    
    db = get_db()
    user = db.users.find_one({'username': data['username']})
    
    if user and check_password_hash(user['password'], data['password']):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


def get_user_data(username):
    db = get_db()
    user_data = list(db.travel_data.find({'user_id': username}, {'_id': 0}))
    
    return jsonify(user_data) 