#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb

    db = MySQLdb.connect(host="localhost",  port=3306,
                        user="root", password="root",
                        database="hbtn_0c_0")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE mydatabase")
    cursor.close()
    db.close()
    