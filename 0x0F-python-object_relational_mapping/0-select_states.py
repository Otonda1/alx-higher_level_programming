#!/usr/bin/python3

""" a script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":

    import MySQLdb
    import sys
    host = 'localhost'
    try:
        db = MySQLdb.connect(host=host, user=sys.argv[1],
                             passwd=sys.argv[2], database=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"MySQLdb Error {e}")

    cur.close()
    db.close()
