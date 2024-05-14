from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.user_service import *
from app.models.user_model import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    expected_keys = {'username', 'password', "admin", "role"}
    payload_keys = set(request.json.keys())
    if not payload_keys.issubset(expected_keys):
        excess_keys = payload_keys - expected_keys
        return jsonify({"msg": f"Unexpected keys in payload: {', '.join(excess_keys)}"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    admin = request.json.get('admin', False)
    role = request.json.get('role', None)
    try:
        register_user(username, password, admin, role)
        return jsonify({"msg": "User created"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 400
    
@auth.route('/login', methods=['POST'])
def login():
    expected_keys = {'username', 'password'}
    payload_keys = set(request.json.keys())
    if not payload_keys.issubset(expected_keys):
        excess_keys = payload_keys - expected_keys
        return jsonify({"msg": f"Unexpected keys in payload: {', '.join(excess_keys)}"}), 400
    
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = get_user_by_username(username)
    if user and check_password(password, user['password']):
        access_token = create_access_token(identity={"username": username, "userId": str(user.id), "role": user.role or "user", "admin": user.admin or False})
        return jsonify(access_token=access_token), 200, {'Content-Type': 'application/json', 'x-access-token': access_token, 'Access-Control-Expose-Headers': 'x-access-token', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'x-access-token'}
    else:
        return jsonify({"msg": "Bad username or password"}), 401
 
@auth.route('/users', methods=['GET'])
@jwt_required()
def users():
    current_user = get_jwt_identity()
    if 'admin' not in current_user or current_user['admin'] != True or 'role' not in current_user or current_user['role'] != 'admin':
        return jsonify({"success": False, "msg": "Unauthorized", "error": "You are not authorized to access this resource"}), 401
    users = get_all_users()
    return jsonify(users), 200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}