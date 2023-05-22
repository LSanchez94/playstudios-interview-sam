import json
from pymongo import MongoClient

client = MongoClient('mongodb+srv://dbLuis:dbLuistest23@test.bjrun4l.mongodb.net/?retryWrites=true&w=majority')
db = client['playstudios']
rewards = db['rewards']

def new_reward(event, context):
    content = event.get('queryStringParameters')
    new_reward = {"name": content['name'], "desc": content['desc'], "price": content["price"], "category": content["category"], "image": content["image"]}
    rewards.insert_one(new_reward)

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps({
            "message": "New Reward Added",
        }),
    }

def update_reward(event, context):
    content = event.get('queryStringParameters')
    last_reward = {"name": content['sname'], "desc": content['sdesc'], "price": content["sprice"], "category": content["scategory"], "image": content["simage"]}
    update_reward ={"$set": {"name": content['name'], "desc": content['desc'], "price": content["price"], "category": content["category"], "image": content["image"]}}
    rewards.update_one(last_reward, update_reward)

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps({
            "message": "Reward Updated",
        }),
    }

def delete_reward(event, context):
    content = event.get('queryStringParameters')
    delete_reward = {"name": content['name'], "desc": content['desc'], "price": content["price"], "category": content["category"], "image": content["image"]}
    rewards.delete_one(delete_reward)

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps({
            "message": "Reward Deleted",
        }),
    }

def rewards_list(event, context):
    result = []
    for x in rewards.find({},{"_id": 0,"name": 1, "desc": 1, "price":1, "category": 1, "image":1}):
        result.append(x)

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
