import cards


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    cards_db.add_card(cards.Card(summary='first'))
    cards_db.add_card(cards.Card(summary='second'))
    assert cards_db.count() == 2
