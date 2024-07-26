# Flask Message API

A simple Flask application providing a RESTful API for managing messages.

# Features

**Create Message**: Add a new message.
**Get Messages by Account ID**: Retrieve messages by account ID.
**Search Messages**: Find messages by message ID, sender number, or receiver number.
**Error Handling**: Handles errors for bad requests, not found resources, and internal server errors.

# Endpoints

**Create Message**

URL: /create
Method: POST

Request Body:

**{
"account_id": "string",
"sender_number": "string",
"receiver_number": "string"
}**

Response:

201: Created message
400: Missing fields or no data

**Get Messages by Account ID**

URL: /get/messages/<account_id>

Method: GET

Response:

200: List of messages

404: No messages found

**Search Messages**

URL: /search

Method: GET

Query Parameters: message_id, sender_number, receiver_number

Response:

200: List of matching messages