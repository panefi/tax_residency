from flask import Blueprint, request, jsonify
from utils import calculate_days_outside
from database import get_db

main = Blueprint('main', __name__)

@main.route('/add_travel', methods=['POST'])
def add_travel():
    data = request.json
    user_id = data['user_id']
    departure_date = data['departure_date']
    return_date = data['return_date']
    country = data['country']
    
    # Calculate days outside
    days_outside = calculate_days_outside(departure_date, return_date)
    
    # Store the travel data in MongoDB
    db = get_db()
    db.travel_data.insert_one({
        'user_id': user_id,
        'departure_date': departure_date,
        'return_date': return_date,
        'country': country,
        'days_outside': days_outside
    })
    
    return jsonify({'days_outside': days_outside})

@main.route('/get_travel_data', methods=['GET'])
def get_travel_data():
    user_id = request.args.get('user_id')
    db = get_db()
    user_travel_data = list(db.travel_data.find({'user_id': user_id}, {'_id': 0}))
    return jsonify(user_travel_data) 