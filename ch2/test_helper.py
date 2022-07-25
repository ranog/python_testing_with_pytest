import pytest

from cards_proj.src.cards.api import Card


def assert_identical(card1: Card, card2: Card):
    __tracebackhide__ = True
    assert card1 == card2
    if card1.id != card2.id:
        pytest.fail(f"id's don't match. {card1.id} != {card2.id}" )


def test_identical():
    card1 = Card(summary='foo', id=123)
    card2 = Card(summary='foo', id=123)
    assert_identical(card1=card1, card2=card2)


def test_identical_fail():
    card1 = Card(summary='foo', id=123)
    card2 = Card(summary='foo', id=456)
    assert_identical(card1=card1, card2=card2)
