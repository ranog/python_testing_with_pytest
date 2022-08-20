import pytest


@pytest.fixture(scope='module')
def to_list():
    print('The Ultimate Question of Life, the Universe and Everything')
    yield ['towel', 42]
    print(' The answer is 42')


@pytest.fixture()
def to_dict():
    """The guide says that the towel is one of the most useful objects for an interstellar backpacker..."""
    return {'towel': 42}


@pytest.fixture()
def to_tuple():
    return ('towel', 42)


def test_to_list(to_list):
    assert to_list == ['towel', 42]


def test_if_it_is_list_type(to_list):
    assert type(to_list) == list


def test_to_dict(to_dict):
    assert to_dict == {'towel': 42}


def test_if_it_is_dict_type(to_dict):
    assert type(to_dict) == dict



def test_to_tuple(to_tuple):
    assert to_tuple == ('towel', 42)


def test_if_it_is_tuple_type(to_tuple):
    assert type(to_tuple) == tuple
