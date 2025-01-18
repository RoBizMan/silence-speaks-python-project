from flask import Blueprint, request, jsonify
from datetime import datetime, timezone

main = Blueprint('main', __name__)


@main.route('/echo', methods=['POST'])
def echo():
    data = request.json
    message = data.get('message', '')
    timestamp = datetime.now(timezone.utc).isoformat()
    return jsonify({'message': message, 'timestamp': timestamp}), 200


@main.route('/echo', methods=['GET'])
def get_echo():
    return jsonify({
        'message': 'Send a POST request with a message.',
        'timestamp': datetime.now(timezone.utc).isoformat()
        }), 200
