from cards_proj.src.cards.api import Card


def test_to_dict():
    # GIVEN a Card object with known contents
    card1 = Card(summary='something', owner='brian', state='todo', id=123)

    # WHEN we call to_dict() on the object
    card2 = card1.to_dict()

    # THEN the result will be a dictionary with known content
    card2_expected = {
        'summary': 'something',
        'owner': 'brian',
        'state': 'todo',
        'id': 123,
    }
    assert card2 == card2_expected
