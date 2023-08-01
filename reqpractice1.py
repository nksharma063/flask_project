from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Hello venv based Flask :D"

@app.route('/course')
def course():
    return 'this is course page'

@app.route('/aboutus')
def aboutus():
    return 'this is about us page'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username=data['username']
    password=data['password']
    if username == 'neeraj' and password == 'neeraj':
        return "Sucess"
    else:
        return "Username and Password is incorrect"

if __name__ == '__main__':
    app.run(port=3000, debug = True)