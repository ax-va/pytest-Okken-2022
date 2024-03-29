from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
import cards


@pytest.fixture(scope="session")
def cards_db():
    """ CardsDB object connected to a temporary database """
    with TemporaryDirectory() as db_dir:
        # SETUP
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        # Pass to tests
        yield db
        # TEARDOWN
        db.close()
    # Clean up the temporary directory
