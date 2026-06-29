#!/usr/bin/python3
"""Lists all city objects from the db by state."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    # Connect to the MySQL server using credentials and db name
    # passed in as command line arguments
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )
    # Create a session to query the database via the ORM
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query States and Cities together, joining on state_id,
    # ordered by city id ascending
    results = session.query(State, City).filter(
        State.id == City.state_id
    ).order_by(City.id).all()

    # Print each result in the format "<state name>: (<city id>) <city name>"
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
