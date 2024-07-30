# FLask Api
## __My **first** python API Server__
__This is a simple API server__

## Main modules used are..
1. ## **Server**
  * **Flask:** Light wieght and highly configurable python web server 
  * **Flask > Blueprint:** This is a submodule (actually a class) in flask used for Flask's creating sub apps. Similar to useRouter in Express
  * **Flask > request:** A method in flask used to access the request object in flask. also similar to request object in express
  * **Flask > jsonify:** A method exposed by flask used in creating json out of an object
2.  ## **Database**
  * **Mongodb:** The best enterprise grade non relational database out there
  * **MongoEnine:** A Module built on top of **PyMongo**. Brings ORM into the picture like **Mongoose**
3.  ## **Authentication and Authorization**
  * **Flask_jwt_extended:** A straight forward and robust module for creating and consuming **JSON Web Tokens (JWT)** in **Python**
  * **flask_bcrypt:** A module for cryptographic purposes. I used this for password hashing and verification

  ## How to Run ##
  __Before you can run the server, make sure you have
  1.  [**python**](https://www.python.org/downlaods) downloaded and installed in your computer__
  2.  Install all the dependcies installed..
   ## in Dev, IT is best to install and run in a virtual environment to avoid curroption of dependecies ##
  * **unix systems:** run __./setup.env.sh__
  * **windows pc:** run __./setup.env.bat__
  ## in production mode, you don't realy care about module corruption so you just install using ## __pip install -r requirements.txt__

  ## Run the app ##
  after installing either in a virtual environment or other wise, run __python main.py__ to start the server.  
  that's it. you should have the server running at (http://127.0.0.1:5000)[http://127.0.0.1:5000] or another port (will be displayed on the console) if port 5000 is already in use