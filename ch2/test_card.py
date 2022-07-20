from cards_proj.src.cards.api import Card


def test_field_access():
    card = Card(summary='something', owner='brian', state='todo', id=123)
    assert card.summary == 'something'
    assert card.owner == 'brian'
    assert card.state == 'todo'
    assert card.id == 123


def test_defaults():
    card = Card()
    assert card.summary is None
    assert card.owner is None
    assert card.state == 'todo'
    assert card.id is None


def test_equality():
    card1 = Card(summary='something', owner='brian', state='todo', id=123)
    card2 = Card(summary='something', owner='brian', state='todo', id=123)
    assert card1 == card2


def test_equality_with_diff_ids():
    card1 = Card(summary='something', owner='brian', state='todo', id=123)
    card2 = Card(summary='something', owner='brian', state='todo', id=4567)
    assert card1 == card2


def test_inequality():
    card1 = Card(summary='something', owner='brian', state='todo', id=123)
    card2 = Card(summary='completely different', owner='okken', state='done', id=123)
    assert card1 is not card2


def test_from_dict():
    card1 = Card(summary='something', owner='brian', state='todo', id=123)
    card2_dict = {'summary': 'something', 'owner': 'brian', 'state': 'todo', 'id': 123}
    card2 = Card.from_dict(card2_dict)
    assert card1 == card2


def test_to_dict():
    card1 = Card(summary='something', owner='brian', state='todo', id=123)
    card2 = card1.to_dict()
    card2_expected = {'summary': 'something', 'owner': 'brian', 'state': 'todo', 'id': 123}
    assert card2 == card2_expected
