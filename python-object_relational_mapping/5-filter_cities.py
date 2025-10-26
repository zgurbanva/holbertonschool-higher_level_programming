#!/usr/bin/python3
"""List all city names of a given state (SQL injection safe) using MySQLdb.

Usage:
    ./5-filter_cities.py <mysql_user> <mysql_pwd> <db_name> <state_name>

Prints a comma-and-space separated list of city names ordered by cities.id.
"""

import sys
import MySQLdb


def main():
    """Connect to MySQL on localhost:3306 and print the state's cities."""
    user, password, db_name, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()

    # Single execute() call; parameterized to prevent SQL injection
    cur.execute(
        ("SELECT cities.name FROM cities "
         "JOIN states ON cities.state_id = states.id "
         "WHERE states.name = %s "
         "ORDER BY cities.id ASC;"),
        (state_name,)
    )

    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
