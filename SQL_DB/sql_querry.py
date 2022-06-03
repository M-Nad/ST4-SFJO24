import sqlite3

db_name = "apprentissage.db"

def db_connection_open(db_name):
    conn = sqlite3.connect(db_name,)
    return conn

def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("Query successful")
    except sqlite3.Error as err:
        print(f"Error: '{err}'")

def db_connection_close(conn):
    conn.close()