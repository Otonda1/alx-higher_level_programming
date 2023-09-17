#!/usr/bin/python3
"""
    a script that lists all states with a name
    starting with N (upper N) from the database hbtn_0e_0_usa:
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    host = 'localhost'

    try:
        db = MySQLdb.connect(host=host, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            if row[1][0] == 'N':
                print(row)
    except MySQLdb.Error as e:
        print(f"errors {e} occured")
    cur.close()
    db.close()
