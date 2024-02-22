import sqlite3

def connect_to_database(database_name):
    try:
        conn = sqlite3.connect(database_name)
        print("Successfully connected to the database")
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def main():
    # Database name
    database_name = "company_xyz.db"
    
    # Connect to the database
    conn = connect_to_database(database_name)
    if conn:
        # Close the connection
        conn.close()
        print("Connection closed")

if __name__ == "__main__":
    main()