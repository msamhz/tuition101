from flask import Flask, jsonify, Response
import socket
import time
import math

app = Flask(__name__)

@app.route('/')
def index():
    """Return a welcome message."""
    return jsonify({"message": f"Welcome to the Flask API! {socket.gethostname()}"})


@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    """Return a greeting with CPU-intensive work."""
    # Simulate CPU-intensive work
    start_time = time.time()
    end_time = start_time + 5  # Run for 5 seconds
    result = 0
    while time.time() < end_time:
        for i in range(1, 10000):
            result += math.sqrt(i)
    
    return jsonify({"message": f"Hello, {name}!", "result": result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
