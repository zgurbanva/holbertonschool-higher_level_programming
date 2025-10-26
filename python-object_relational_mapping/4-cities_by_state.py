#!/usr/bin/python3
"""List all cities with their state names from a MySQL database using MySQLdb.

Usage:
    ./4-cities_by_state.py <mysql_user> <mysql_pwd> <db_name>

Outputs tuples: (city_id, city_name, state_name), ordered by cities.id ASC.
"""

import sys
import MySQLdb


def main():
    """Connect to localhost:3306 and print all cities with their states."""
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

    # Single execute() call
    cur.execute(
        ("SELECT cities.id, cities.name, states.name "
         "FROM cities JOIN states ON cities.state_id = states.id "
         "ORDER BY cities.id ASC;")
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
