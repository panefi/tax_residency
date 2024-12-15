from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db
from flask import jsonify

def register_user(data):
    username = data['username']
    password = data['password']
    
    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')
    
    # Store the user in the database
    db = get_db()
    db.users.insert_one({
        'username': username,
        'password': hashed_password
    })
    
    return jsonify({'message': 'User registered successfully'}), 201

def login_user(data):
    username = data['username']
    password = data['password']
    
    db = get_db()
    user = db.users.find_one({'username': username})
    
    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

def get_user_data(username):
    db = get_db()
    user_data = list(db.travel_data.find({'user_id': username}, {'_id': 0}))
    
    return jsonify(user_data) 