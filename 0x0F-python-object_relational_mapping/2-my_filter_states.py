#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the states
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    name = sys.argv[4]
    localhost = 'localhost'
    try:
        db = MySQLdb.connect(host=localhost, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name = %s", (name,))
        row = cur.fetchall()
        print(row)

    except MySQLdb.Error as e:
        print(f"MySQLdb error: {e}")

    finally:
        cur.close()
        db.close()
