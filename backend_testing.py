
import requests
import db_connector



test_id = '78'
name = 'Simon'
test_url = f'http://127.0.0.1:5000/users/{test_id}'


res = requests.post(test_url, json={'user_name': name })
if not res.ok:
    print(f"POST failed: {res.status_code} - {res.text}")
else:
    print('User name successfully created')
    #exit()


request_user = requests.get(test_url)
if request_user .status_code == 200:
    get_data = request_user.json()
    print(get_data)

    if get_data.get('user_name') == name:
        db_user = get_data.get('user_name')
        print(f'Successfully matched {db_user}')




conn = db_connector.get_db_connection()
#cursor = conn.cursor()
try:
    with conn.cursor() as cursor:
        user_in_db = f"SELECT user_name FROM users WHERE user_id = {test_id}"
        cursor.execute(user_in_db)
        db_results = cursor.fetchone()

        if db_results:
            db_user_name = db_results[0]
            print("Database check: User name in DB:", db_user_name)
            if db_user_name == name:
                print("Database check: Data matches posted data!")
            else:
                print(f"Database check: Data mismatch! Expected '{name}', got '{db_user_name}'")
        else:    print(
            "Database check: User not found in the database.")

            # put an exception to show error if data exist already.  refer back to error handling lesson

finally:
    if conn:
        conn.close()
