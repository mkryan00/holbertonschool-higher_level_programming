#!/usr/bin/python3
"""Adds the state object Louisiana to the database."""

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

    # Instantiate new state, named Louisiana.
    new_state = State(name="Louisiana")

    # Stage the new state object to be added to the session
    session.add(new_state)

    # Commit the transaction, saving the new state to the
    # database and auto-generating its id
    session.commit()

    # Print new state's id
    print(new_state.id)

    # Close the session
    session.close()
