import sqlite3
import csv

def initialize_database():
    # Connect to the SQLite database
    conn = sqlite3.connect("database/user_details.db")
    c = conn.cursor()

    with conn:
        # Create the 'users' table if it doesn't exist (Note: Storing plaintext passwords is not secure)
        c.execute("""CREATE TABLE IF NOT EXISTS users (
                            userid INTEGER PRIMARY KEY,
                            firstname TEXT,
                            lastname TEXT,
                            username TEXT,
                            password TEXT
                        )""")
        
        # Check if the 'users' table is empty
        c.execute('SELECT COUNT(*) FROM users')
        count = c.fetchone()

        # If the table is empty, populate it with sample data from a CSV file
        if count is not None and count[0] == 0:
            with open('data/sample_data.csv', 'r') as dataFile:
                dataReader = csv.reader(dataFile)

                # Loop through the CSV data and insert it into the 'users' table
                for row in dataReader:
                    c.execute("""INSERT INTO users (firstname, lastname, username, password)
                                    VALUES (:fName, :lName, :uName, :pwd)""",
                                    {'fName' : row[0], 'lName' : row[1], 'uName' : row[2], 'pwd' : row[3]})


