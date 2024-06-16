from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Return a welcome message."""
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    """Return a greeting."""
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)