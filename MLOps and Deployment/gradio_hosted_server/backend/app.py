from flask import Flask, jsonify
import socket 

app = Flask(__name__)

@app.route('/')
def index():
    """Return a welcome message."""
    return jsonify({"message": f"Welcome to the Flask API! {socket.gethostname()}"})


@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    """Return a greeting."""
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)