from cards_proj.src.cards.api import Card


def test_equality_fail():
    card1 = Card(summary='sit there', owner='brain')
    card2 = Card(summary='do something', owner='okken')
    assert card1 == card2


if __name__ == '__main__':
    test_equality_fail()
