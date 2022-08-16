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


@pytest.fixture(scope='session')
def some_cards():
    '''List of different Card objects'''
    return [
        cards.Card(summary='write book', owner='Brian', state='done'),
        cards.Card(summary='edit book', owner='Katie', state='done'),
        cards.Card(summary='write 2nd edition', owner='Brian', state='todo'),
        cards.Card(summary='edit 2nd edition', owner='Katie', state='todo'),
    ]


@pytest.fixture(scope='function')
def non_empty_db(cards_db, some_cards):
    """CardsDB object that's been populated with 'some_cards"""
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db
