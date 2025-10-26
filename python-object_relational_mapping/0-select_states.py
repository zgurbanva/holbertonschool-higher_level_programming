#!/usr/bin/python3
"""List all states from a MySQL database using MySQLdb.

The script takes MySQL credentials and a database name as arguments and
prints each row of the `states` table as a tuple, ordered by id ascending.
"""

import sys
import MySQLdb


def main():
    """Connect to MySQL on localhost:3306 and list all states ordered by id."""
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
