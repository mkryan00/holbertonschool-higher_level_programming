#!/usr/bin/python3
"""Changes the name of a state object in the database."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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

    # Find the State with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Update its name to New Mexico and save the change
    if state is not None:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
