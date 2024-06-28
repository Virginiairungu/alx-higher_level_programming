#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa. """
import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py root C@m3R00n#2050# hbtn_0e_0_usa")
        sys.exit(1)
    
    # Database connection
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
