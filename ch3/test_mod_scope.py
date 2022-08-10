import pytest
from pathlib import Path
from tempfile import TemporaryDirectory

import cards


@pytest.fixture(scope='module')
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    cards_db.add_card(cards.Card(summary='first'))
    cards_db.add_card(cards.Card(summary='second'))
    assert cards_db.count() == 2
