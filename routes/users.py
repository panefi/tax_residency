from flask import Blueprint, request
from services.user_service import register_user, login_user, get_user_data

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/')
def user_home():
    """
    User Home
    ---
    tags:
      - users
    responses:
      200:
        description: Returns a welcome message for the user home
    """
    return "User Home"

@users_blueprint.route('/register', methods=['POST'])
def register():
    """
    Register a new user
    ---
    tags:
      - users
    parameters:
      - name: username
        in: body
        type: string
        required: true
        description: The username for the new user
      - name: password
        in: body
        type: string
        required: true
        description: The password for the new user
    responses:
      201:
        description: User registered successfully
    """
    return register_user(request.json)

@users_blueprint.route('/login', methods=['POST'])
def login():
    """
    User login
    ---
    tags:
      - users
    parameters:
      - name: username
        in: body
        type: string
        required: true
        description: The username of the user
      - name: password
        in: body
        type: string
        required: true
        description: The password of the user
    responses:
      200:
        description: Login successful
      401:
        description: Invalid username or password
    """
    return login_user(request.json)

@users_blueprint.route('/user_data', methods=['GET'])
def user_data():
    """
    Get user data
    ---
    tags:
      - users
    parameters:
      - name: username
        in: query
        type: string
        required: true
        description: The username of the user
    responses:
      200:
        description: User data retrieved successfully
    """
    username = request.args.get('username')
    return get_user_data(username)
