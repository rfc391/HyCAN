
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/analytics', methods=['GET'])
def analytics():
    # Mock analytics data
    data = {
        "active_users": 120,
        "model_accuracy": 95.2,
        "average_response_time": "120ms"
    }
    return jsonify(data)

if __name__ == '__main__':
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)
