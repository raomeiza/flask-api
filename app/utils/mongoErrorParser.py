# create a function that parses mongo engine errors and returns a human-readable message. The function should accept an exception as an argument and return an object with a message key. The message should be a string that describes the error.

def parse_mongo_error(error):
    if 'duplicate key error' in str(error):
        return {
            "message": "User already exists",
            "status": "409"
            }
    return {"message": "An error occurred"}