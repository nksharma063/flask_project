from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

@app.route('/')
def Home():
    return "This is the home page"

@app.route('/registration', methods = ['POST'])
def registration():
    result = request.form
    with open('abc.csv', 'a') as file:
        # for key,value in result.items():
        writer = csv.writer(file)
        if os.stat('abc.csv').st_size == 0:
            writer.writerow(['username', 'password', 'email'])
        writer.writerow([result['username'], result['password'], result['email']])
    return 'sucess'

if __name__ == '__main__':
    app.run(port=3000, debug=True) 


