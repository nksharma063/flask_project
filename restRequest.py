from flask import Flask, jsonify
from pymongo import MongoClient
import json, os

app = Flask(__name__)

client = MongoClient(os.environ.get('MONGO_URI'))
db = client.PythonAssignment

database = db.get_collection('databaseCred')
server = db.get_collection('serverCred')

@app.route("/", methods = ["GET"])
def get_PythonAssignment():
    databaseDocs = database.find_one({'_id':False})
    serverDocs = server.find_one({{'_id':False}})
    return jsonify({'databaseDocs': databaseDocs, 'serverDocs':serverDocs})


if __name__ == "__main__":
    app.run(port=3000, debug=True)
   
