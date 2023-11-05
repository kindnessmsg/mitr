import sqlite3

def authenticate_user(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('database/user_details.db')
    cursor = conn.cursor()

    # Execute a SQL query to check if a user with the given username and password exists
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Return True if a user was found, indicating successful authentication
    return user is not None
