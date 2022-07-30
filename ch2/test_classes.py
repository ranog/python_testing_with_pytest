from cards_proj.src.cards.api import Card


class TestEquality:
    def test_equality(self):
        card1 = Card(summary='something', owner='brian', state='todo', id=123)
        card2 = Card(summary='something', owner='brian', state='todo', id=123)
        assert card1 == card2

    def test_equality_with_diff_ids(self):
        card1 = Card(summary='something', owner='brian', state='todo', id=123)
        card2 = Card(summary='something', owner='brian', state='todo', id=4567)
        assert card1 == card2

    def test_inequality(self):
        card1 = Card(summary='something', owner='brian', state='todo', id=123)
        card2 = Card(summary='completely different', owner='okken', state='done', id=123)
        assert card1 != card2
