from flask import Flask, request
import db_connector

app = Flask(__name__)
conn = db_connector.get_db_connection()

#Supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def users(user_id):
    if request.method == 'GET':
        # Retrieve user data from the database
        cursor = conn.cursor()
        db_user = f"SELECT user_name FROM users WHERE user_id = '{user_id}'"
        cursor.execute(db_user)
        result = cursor.fetchone()

        if result:
            get_user_name = result[0]
            return {"User ID: {user_id}, User Name: {get_user_name}"}, 200
        else:
            return {"User with ID '{user_id}' not found"}, 404

    elif request.method == 'POST':

        # Save user data to the database
        request_data = request.json
        user_name = request_data.get('user_name')

        if not user_name:
            return "Missing required field: user_name", 400

        cursor = conn.cursor()

        # Check for existing user ID
        db_user = f"SELECT * FROM users WHERE user_id = '{user_id}'"
        cursor.execute(db_user)
        existing_user = cursor.fetchone()

        if existing_user:
            return {"status": "error", "reason": "ID already exists"}, 500

            # If ID is unique, proceed with insertion
        db_user = f"INSERT INTO users (user_id, user_name) VALUES ('{user_id}', '{user_name}')"
        cursor.execute(db_user)
        return f"User ID: {user_id}, User Name: {user_name} saved", 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)