#!/usr/bin/python3
""" filter from the database hbtn_0e_0_usa based on user input"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id;",(sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
cur.close()
db.close()
