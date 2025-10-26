#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' (uppercase) from a MySQL database.

Usage:
    ./1-filter_states.py <mysql_username> <mysql_password> <database_name>

Requirements:
- Uses MySQLdb (Python3 MySQL client)
- Connects to localhost on port 3306
- Results sorted by states.id (ascending)
- Prints rows exactly like: (id, 'Name')
- Code is not executed when imported
"""
import sys
import MySQLdb


def main():
    """Connects to MySQL, queries states starting with 'N', and prints results."""
    usr, pwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        passwd=pwd,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()

    # Use BINARY to enforce case-sensitivity on the first character ('N%')
    cur.execute(
        "SELECT id, name FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC;"
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
