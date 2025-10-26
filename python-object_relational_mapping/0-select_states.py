#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa using MySQLdb.
Usage: ./0-select_states.py <mysql_user> <mysql_password> <database_name>
Results are sorted by states.id in ascending order and printed as tuples.
"""

import sys
import MySQLdb


def main():
    """Connects to MySQL and prints all rows from states ordered by id ASC."""
    user, passwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
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
