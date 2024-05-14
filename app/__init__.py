import datetime
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from mongoengine import connect
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '37452v8345827h5828523'  # Change this
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

connect(db='myDatabase2', host='localhost', port=27017)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from app.controllers.user_controller import auth

app.register_blueprint(auth)