from flask import Flask, jsonify
from pymongo import MongoClient
import json, os


app = Flask(__name__)

client = MongoClient('mongodb+srv://nksharma063:Her0V1red%4012345@cluster0.gdlcigy.mongodb.net/')
db = client.PythonAssignment

database = db.get_collection('databaseCred')
server = db.get_collection('serverCred')

@app.route("/", methods = ["GET"])
def get_PythonAssignment():
    databaseDocs = database.find_one({})
    serverDocs = server.find_one({})
    return {databaseDocs, serverDocs}


if __name__ == "__main__":
    app.run(port=3000, debug=True)
   
