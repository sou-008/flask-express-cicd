from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    # Return a JSON response with a new message
    return jsonify({"message": "Welcome to my Flask app! The server is running successfully."})

if __name__ == '__main__':
    # Run the Flask app and listen on all available network interfaces (0.0.0.0) at port 5000
    app.run(host='0.0.0.0', port=5000)
