#!/usr/bin/python3
"""Delete all state objects containing letter 'a'."""

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

    # Find states with the letter 'a' in them.
    states = session.query(State).filter(
        State.name.like('%a%')
    ).delete()

    # Commit the change, saving the updated database.
    session.commit()

    # Close the session
    session.close()
