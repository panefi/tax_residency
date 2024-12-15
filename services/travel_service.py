from database import get_db
from flask import jsonify

def get_travel_data(user_id):
    db = get_db()
    travel_data = list(db.travel_data.find({'user_id': user_id}, {'_id': 0}))
    return jsonify(travel_data)

def add_travel_entry(user_id, entry):
    db = get_db()
    db.travel_data.insert_one({
        'user_id': user_id,
        **entry
    })
    return jsonify({'message': 'Travel entry added successfully'}), 201 