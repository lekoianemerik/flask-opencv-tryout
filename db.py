from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://<username>:<password>@flask-mongodb-atlas-1g8po.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('<your_db_name>')
user_collection = pymongo.collection.Collection(db, '<your_collection_name>')