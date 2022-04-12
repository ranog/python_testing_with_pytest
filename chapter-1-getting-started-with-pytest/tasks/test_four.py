"""Test the Task data tupe."""

from collections import namedtuple

Task = namedtuple(typename='Task', field_names=['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    """_asdict() should return a dictionary."""
    task = Task(summary='do something', owner='Okken', done=True, id=21)
    task_dict = task._asdict()
    expected = {'summary': 'do something', 'owner': 'Okken', 'done': True, 'id': 21}

    assert task_dict == expected


def test_replace():
    """replace() should change passed in fields."""
    task_before = Task(summary='finish book', owner='Brian', done=False)
    task_after = task_before._replace(id=10, done=True)
    task_expected = Task(summary='finish book', owner='Brian', done=True, id=10)

    assert task_after == task_expected
