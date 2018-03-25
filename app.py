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

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

