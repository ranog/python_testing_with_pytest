from pathlib import Path
from tempfile import TemporaryDirectory
import pytest

import cards


@pytest.fixture(scope='session')
def db():
    '''CardsDB object connected to a temporary database'''
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        _db = cards.CardsDB(db_path)
        yield _db
        _db.close()


@pytest.fixture(scope='function')
def cards_db(db):
    """CardsDB object that's empty"""
    db.delete_all()
    return db
