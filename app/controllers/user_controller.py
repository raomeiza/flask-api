from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.user_service import *
from app.models.user_model import User
from marshmallow import Schema, fields, ValidationError
import json
auth = Blueprint('auth', __name__)

class userSchema(Schema):
    username = fields.Email(required=True)
    password = fields.Str(required=True)
    # repeatPassword should be thesame as password
    repeatPassword = fields.Str(required=True)
    admin = fields.Bool(required=False)
    role = fields.Str(required=False)

class loginSchema(Schema):
    username = fields.Email(required=True)
    password = fields.Str(required=True)
    
@auth.route('/register', methods=['POST'])
def register():
    try:
        userSchema().load(request.json)
    except ValidationError as e:
        return jsonify({"msg": str(e)}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    repeatPassword = request.json.get('repeatPassword', None)
    admin = request.json.get('admin', False)
    role = request.json.get('role', None)

    if password != repeatPassword:
        return jsonify({"msg": "Passwords do not match"}), 400
    
    try:
        register_user(username, password, admin, role)
        return jsonify({"msg": "User created"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 400
    
@auth.route('/login', methods=['POST'])
def login():
    try:
        loginSchema().load(request.json)
    except ValidationError as e:
        return jsonify({"msg": str(e)}), 400
    
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = get_user_by_username(username)
    if user and check_password(password, user['password']):
        access_token = create_access_token(identity={"username": username, "userId": str(user.id), "role": user.role or "user", "admin": user.admin or False})
        return jsonify(access_token=access_token), 200, {'Content-Type': 'application/json', 'x-access-token': access_token, 'Access-Control-Expose-Headers': 'x-access-token', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'x-access-token'}
    else:
        return jsonify({"msg": "Bad username or password", "user": json.loads(user.to_json())}), 401 
@auth.route('/users', methods=['GET'])
@jwt_required()
def users():
    current_user = get_jwt_identity()
    if 'admin' not in current_user or current_user['admin'] != True or 'role' not in current_user or current_user['role'] != 'admin':
        return jsonify({"success": False, "msg": "Unauthorized", "error": "You are not authorized to access this resource"}), 401
    users = get_all_users()
    return jsonify(users), 200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}