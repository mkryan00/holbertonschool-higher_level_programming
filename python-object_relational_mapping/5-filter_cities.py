#!/usr/bin/python3
"""A script that lists all citie of state that is provided."""

import sys
import MySQLdb

# Connect to the MySQL server using credentials and db name
# passed in as command line arguments
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor to execute SQL commands and fetch results
    cursor = db.cursor()

    # Join cities with their corresponding state name,
    # matching cities.state_id to states.id,
    # ordered by city id ascending
    cursor.execute(
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
    )

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Print each row (each row is a tuple, e.g. (1, 'California'))
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    # Close the cursor and the database connection
    cursor.close()

    db.close()
