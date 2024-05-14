# from flask import Flask, request, jsonify
# # from flask_cors import CORS
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# app = Flask(__name__)

# app.config['JWT_SECRET_KEY'] = '37452v8345827h5828523'
# jwt = JWTManager(app)

# @app.route('/hello', methods=['GET'])
# def hello():
#     return "Hello World!"

# @app.route('/hello/<name>', methods=['GET'])
# def great(name):
#     queries = request.args.to_dict()
#     data = jsonify(queries)
#     return data, 200

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)

#     if username != 'test' or password != 'test':
#         return jsonify({"msg": "Bad username or password"}), 401

#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token), 200

# @app.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     # get x-auth-token from header
#     token = request.headers.get('x-auth-token')
#     return jsonify(logged_in_as=current_user), 200, {'x-auth-token': token}

# if __name__ == '__main__':
#     app.run(debug=True)

from app import app

if __name__ == '__main__':
    app.run(debug=True)