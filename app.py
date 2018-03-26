from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from random import randint
@app.route('/')
def hello_world():
    return 'Hello, World!' + str(randint(0, 10000))

@app.route('/api/test/')
def hello_world_test():
    return jsonify([{"dat": 'Hello, World!' + str(randint(0, 10000))}])

@app.route('/api/leaderboard/')
def get_leaderboard():
    data = [
        { "username": 'Mod', "dom_points": 44 },
        { "username": 'Dom', "dom_points": 45 },
        { "username": 'Some other guy', "dom_points": 25 },
        { "username": 'Some guy', "dom_points": 20 },
        { "username": 'Me', "dom_points": 4 }]
    return jsonify(data)

@app.route('/api/bets/current/')
def get_current_bets():
    data = [
        { "initiator": 'Mod', "description": 'bleh', "dom_points": 4 },
        { "initiator": 'Mod', "receiver": 'Dom', "description": 'bleh :(', "dom_points": 2 },
        { "initiator": 'Dom', "receiver": 'Some other guy', "description": 'An awful bet', "dom_points": 1 },
        { "initiator": 'Mod', "receiver": 'Some guy', "description": 'How did this even get approved?', "dom_points": 2 },
        { "initiator": 'Mod', "receiver": 'Me', "description": '>.>', "dom_points": 1 }]
    return jsonify(data)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
