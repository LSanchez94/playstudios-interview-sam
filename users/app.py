import json
import jwt
from pymongo import MongoClient


client = MongoClient('mongodb+srv://dbLuis:dbLuistest23@test.bjrun4l.mongodb.net/?retryWrites=true&w=majority')
db = client['playstudios']
users = db['users']

def login(event, context):
    content = event.get('queryStringParameters')
    passwdjwt = jwt.encode({"bearer": content['passwd']}, "test123", algorithm="HS256")
    user = {"username": content['username'], "passwd": passwdjwt}
    result = users.find_one(user,{"_id": 0,"username": 1, "passwd": 1})


    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps({
            "data": result,
        }),
    }

def register(event, context):
    content = event.get('queryStringParameters')
    passwdjwt = jwt.encode({"bearer": content['passwd']}, "test123", algorithm="HS256")
    new_user = {"username": content['username'], "passwd": passwdjwt}
    users.insert_one(new_user)

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps({
            "message": "New User Added",
        }),
    }

def check_token(event, context):
    content = event.get('queryStringParameters')
    passwdjwtdeco = jwt.decode(content['passwd'], "test123", algorithms=["HS256"])
    passwdjwt = jwt.encode(passwdjwtdeco, "test123", algorithm="HS256")
    user = {"username": content['username'], "passwd": passwdjwt}
    result = users.find_one(user,{"_id": 0,"username": 1, "passwd": 1})
    
    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps({
            "data": result,
        }),
    }
