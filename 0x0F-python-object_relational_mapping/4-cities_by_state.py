#!/usr/bin/python3

"""
    a script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    try:
        cur.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities INNER JOIN states ON cities.state_id=states.id\
                    ORDER BY\
                    cities.id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQLdb Error: {}".format(e))

    finally:
        cur.close()
        db.close()
