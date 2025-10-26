#!/usr/bin/python3
"""List all states whose name starts with 'N' (uppercase), sorted by id.

Usage:
    ./1-filter_states.py <mysql_user> <mysql_password> <database>
Connects to localhost:3306 and prints rows as (id, 'Name') tuples.
"""

import sys
import MySQLdb


def main():
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, passwd=pwd, db=db, charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
