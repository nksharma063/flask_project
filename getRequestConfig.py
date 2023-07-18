from automateConfig import *
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/getData/<file>')
def getData(file):
    return getJSON(file)


if __name__ == '__main__':
    app.run(debug=True)