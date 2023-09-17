#!/usr/bin/python3
"""
     a script that takes in the
     name of a state as an argument and lists all cities
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    state = sys.argv[4]
    try:

        db = MySQLdb.connect(host='localhost',
                             user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT cities.name\
                    FROM cities JOIN states ON\
                    cities.state_id=states.id\
                    WHERE states.name= %s\
                    ORDER BY cities.id", (state,))
        i = 0
        query_rows = cur.fetchall()
        for row in query_rows:
            if i > 0:
                print(", ", end="")
            print(row[0], end="")
            i += 1
        print("")
    except MySQLdb.Error as e:
        print("MySQLdbERROR: {}".format(e))

    finally:
        cur.close()
        db.close()
