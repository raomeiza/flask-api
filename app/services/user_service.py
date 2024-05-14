from app import bcrypt
from app.models.user_model import User
from app.utils.mongo_to_dict import mongo_to_dict

def register_user(username, password, admin, role):
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username = username, password = password_hash, admin = admin, role = role).save()
    return user

def get_user_by_username(username):
    return User.objects(username=username).first()

def get_all_users():
    users = User.objects().only('username', 'id')
    users_list = [mongo_to_dict(user, ['password']) for user in users]
    return users_list

def get_user_by_id(user_id):
    return User.objects(id=user_id).first()

def check_password(password, password_hash):
    return bcrypt.check_password_hash(password_hash, password)