from flask import Blueprint, request
from services.travel_service import get_travel_data, add_travel_entry

travel_blueprint = Blueprint('travel', __name__)

@travel_blueprint.route('/data', methods=['GET'])
def travel_data():
    """
    Get travel data
    ---
    tags:
      - travel
    parameters:
      - name: user_id
        in: query
        type: string
        required: true
        description: The user ID to retrieve travel data for
    responses:
      200:
        description: Travel data retrieved successfully
    """
    user_id = request.args.get('user_id')
    return get_travel_data(user_id)

@travel_blueprint.route('/entry', methods=['POST'])
def travel_entry():
    """
    Add a travel entry
    ---
    tags:
      - travel
    parameters:
      - name: user_id
        in: body
        type: string
        required: true
        description: The user ID for the travel entry
      - name: entry
        in: body
        type: object
        required: true
        description: The travel entry details
    responses:
      201:
        description: Travel entry added successfully
    """
    data = request.json
    user_id = data['user_id']
    entry = data['entry']
    return add_travel_entry(user_id, entry) 