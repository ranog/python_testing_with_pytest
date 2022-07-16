import pytest


@pytest.mark.xfail()
def test_it_should_check_if_number_one_is_on_the_list():
    assert 1 in [2, 3, 4]


def test_it_should_check_if_a_is_less_than_b():
    a = 1
    b = 2
    assert a < b


@pytest.mark.xfail()
def test_it_should_check_if_fizz_is_in_the_string():
    assert 'fizz' not in 'fizzbuzz'
