# FLask Api
## __My **first** python API Server__
__This is a simple API server__

## Main modules used are..
1. ## **Server**
  * **Flask:** Light wieght and highly configurable the server
  * **Flask > Blueprint:** This is a submodule (actually a class) in flask used for Flask's creating sub apps. Similar to useRouter in Express
  * **Flask > request:** A method in flask used to access the request object in flask. also similar to request object in express
  * **Flask > jsonify:** A method exposed by flask used in creating json out of an object
2.  ## **Database**
  * **Mongodb:** The best enterprise grade non relational database out there
  * **MongoEnine:** A Module built on top of **PyMongo**. Brings ORM into the picture like **Mongoose**
3.  ## **Authentication and Authorization**
  * **Flask_jwt_extended:** A straight forward and robust module for creating and consuming **JSON Web Tokens (JWT)** in **Python**
  * **bcrypt:** A module for cryptographic purposes. I used this for password hashing and verification