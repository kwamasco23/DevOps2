
from flask import Flask
import pymysql

import db_connector

app = Flask(__name__)

schema_name = "mydb"


conn = db_connector.get_db_connection()

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_data(user_id):

    cursor = conn.cursor()

    try:
        cursor.execute("SELECT name FROM users1 WHERE id = %s", (user_id,))
        result = cursor.fetchone()

        if result:
            user_name = result[0]
            return f"<H1 id='user'>{user_name}</H1>", 200
        else:
            return "<H1 id='user'>No such user</H1>", 404

    finally:
        cursor.close()
        conn.close()





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)