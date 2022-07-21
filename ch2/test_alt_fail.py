import pytest

from cards_proj.src.cards.api import Card


def test_with_fail():
    card1 = Card(summary='sit there', owner='brian')
    card2 = Card(summary='do something', owner='okken')
    if card1 is not card2:
        pytest.fail("they don't match")
