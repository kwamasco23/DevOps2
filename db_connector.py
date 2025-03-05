import pymysql
#
# schema_name = "mydb"
#
# # Establishing a connection to DB
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='Password', db=schema_name)
# conn.autocommit(True)
#
# # Getting a cursor from Database
# cursor = conn.cursor()
#
# # Inserting data into table
# statementToExecute = "CREATE TABLE `" + schema_name + "`.`users`(`user_id` INT NOT NULL,`user_name` VARCHAR(50) NOT NULL,`creation_date` DATETIME DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (`user_id`));"
# cursor.execute(statementToExecute)
#
#
#
#
# cursor.close()
# conn.close()



def get_db_connection():
    schema_name = "mydb"
    try:
        conn= pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='user',
            passwd='Password',
            db=schema_name,
            autocommit=True)
        conn.autocommit(True)
        return conn
    except pymysql.Error as a:
        print(f"Connection not established {a}")
        return None

if __name__ == "__main__":
    conn = get_db_connection()