from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory data store
messages = []


# Error handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


# Routes
@app.route('/get/messages/<account_id>', methods=['GET'])
def get_messages(account_id):
    account_messages = [msg for msg in messages if msg['account_id'] == account_id]
    if not account_messages:
        return jsonify({"error": "No messages found for this account ID"}), 404
    return jsonify(account_messages), 200


@app.route('/create', methods=['POST'])
def create_message():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    account_id = data.get('account_id')
    sender_number = data.get('sender_number')
    receiver_number = data.get('receiver_number')

    if not account_id or not sender_number or not receiver_number:
        return jsonify({"error": "Missing required fields"}), 400

    new_message = {
        "account_id": account_id,
        "message_id": str(uuid.uuid4()),
        "sender_number": sender_number,
        "receiver_number": receiver_number
    }
    messages.append(new_message)

    return jsonify(new_message), 201

@app.route('/search', methods=['GET'])
def search_messages():
    message_ids = request.args.get('message_id')
    sender_numbers = request.args.get('sender_number')
    receiver_numbers = request.args.get('receiver_number')

    filtered_messages = messages

    if message_ids:
        message_ids = message_ids.split(',')
        filtered_messages = [msg for msg in filtered_messages if msg['message_id'] in message_ids]

    if sender_numbers:
        sender_numbers = sender_numbers.split(',')
        filtered_messages = [msg for msg in filtered_messages if msg['sender_number'] in sender_numbers]

    if receiver_numbers:
        receiver_numbers = receiver_numbers.split(',')
        filtered_messages = [msg for msg in filtered_messages if msg['receiver_number'] in receiver_numbers]

    return jsonify(filtered_messages), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
