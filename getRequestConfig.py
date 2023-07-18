
"""
Only problem from this code is that it is fetching teh data from the code and not from the database for now, so when it executes, it read the file and create ultiple entries in database.
SO now we will create one get request using pymongo and flask in next code

"""

from automateConfig import *
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/getData/<file>')
def getData(file):
    return getJSON(file)


if __name__ == '__main__':
    app.run(debug=True)