#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost",
                         user=mysql_user,
                         passwd=mysql_password,
                         db=db_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the result of the query
    rows = cursor.fetchall()  # Fixed typo here

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
