#!/usr/bin/python3
""" Script that lists all states with
a name starting with N from the database
hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost",  port=3306,
                        user=sys.argv[1], password=sys.argv[2],
                        database=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for item in rows:
        if item[1][0] == 'N':
            print(item)
    cursor.close()
    db.close()