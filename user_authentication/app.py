'''
Flask app module for serving the user authentication API.
'''

from flask import Flask, request, jsonify, session
from flask_cors import CORS
from auth import register_user, login_user
from auth_protector import login_required

app = Flask(__name__)
app.secret_key = 'super_duper_secret_key'  # Probably should replace this
CORS(app)

@app.route('/register', methods=['POST'])
def api_register_user():
    '''
    API endpoint to register a new user.
    '''
    data = request.get_json()
    username = data['username']
    password = data['password']

    success, message = register_user(username, password)
    if success:
        return jsonify({"message": message}), 201
    return jsonify({"message": message}), 400

@app.route('/login', methods=['POST'])
def api_login_user():
    '''
    API endpoint to log in a user.
    '''
    data = request.get_json()
    username = data['username']
    password = data['password']

    success, message = login_user(username, password)
    if success:
        session['logged_in'] = True
        session['username'] = username
        return jsonify({"message": message}), 200
    else:
        session['logged_in'] = False
        return jsonify({"message": message}), 401

@app.route('/protected', methods=['GET'])
@login_required
def protected_route():
    '''
    A protected route that requires a user to be logged in.
    '''
    return jsonify({"message": "You are viewing a protected route!"}), 200

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Should proabaly use a real SSL context in production
