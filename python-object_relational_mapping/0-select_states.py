#!/usr/bin/python3
"""List all states from the given MySQL database ordered by states.id."""
import sys
import MySQLdb


def main():
    """Connect to MySQL on localhost:3306 and print rows from the states table ordered by id."""
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, passwd=passwd, db=db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
