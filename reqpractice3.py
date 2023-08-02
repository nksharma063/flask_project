from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import json_util


client = MongoClient('mongodb+srv://nksharma063:Her0V1red%4012345@cluster0.gdlcigy.mongodb.net/')
db = client['testing']
collection1 = db['RegistrationDetails']

db1 = client['PythonAssignment']
collection2 = db1.get_collection('databaseCred') 


app = Flask(__name__)

@app.route('/')
def Home():
    return "This is the home , kindly register your self"

@app.route('/registration', methods = ['POST'])
def registration():
    result = request.json
    collection1.insert_one(result)
    return "Document added succesfully in RegisrationDetails"
    
@app.route('/login')
def login():
    items = list(collection1.find({}, {'_id':0}))
    return jsonify(items)
    # return json_util.dumps(items)


@app.route('/getQuery')
def getQuery():
    items = list(collection2.find({}, {'_id':0}).sort([('_id', -1)]).limit(1))
    # return json_util.dumps(items)
    return jsonify("database :",items)


if __name__ == "__main__":
    app.run( port=3000, debug= True)

"""
from bson import ObjectId

doc_id = "5f8d0d55f8a5d84ac3a71a21"
doc = collection1.find_one({"_id": ObjectId(doc_id)})


from flask import Flask
from bson import json_util
app = Flask(__name__)

playing with iitems

@app.route('/login')
def login():
    server_item = server.find({}, {'_id': 0}).sort([('_id', -1)]).limit(1)
    database_item = database.find({}, {'_id': 0}).sort([('_id', -1)]).limit(1)
    result = {
        "server": server_item[0] if server_item.count() > 0 else None,
        "database": database_item[0] if database_item.count() > 0 else None
    }
    return json_util.dumps(result)

if __name__ == "__main__":
    app.run(port=3000, debug=True)

    

from flask import Flask
from bson import json_util
app = Flask(__name__)

Playing with dayabse

@app.route('/login')
def login():
    server_items = list(server.find({}))
    database_items = list(database.find({}))
    result = {
        "server": server_items,
        "database": database_items
    }
    return json_util.dumps(result)

if __name__ == "__main__":
    app.run(port=3000, debug=True)

    
    from bson import ObjectId

    
Plaing with object ID

# Create a new ObjectId
new_id = ObjectId()

# Convert an ObjectId to a string
id_str = str(new_id)

# Convert a string to an ObjectId
id_obj = ObjectId(id_str)

# Compare two ObjectIds
if new_id == id_obj:
    print("The ObjectIds are equal")
else:
    print("The ObjectIds are not equal")


"""