"""Test the Task data type."""
from collections import namedtuple

Task = namedtuple(typename='Task', field_names=['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Using no parameters should invoke defaults."""
    task_1 = Task()
    task_2 = Task(summary=None, owner=None, done=False, id=None)

    assert task_1 == task_2


def test_member_access():
    """Check .field functionality of namedtuple."""
    task = Task(summary='buy milk', owner='Brian')

    assert task.summary == 'buy milk'
    assert task.owner == 'Brian'
    assert (task.done, task.id) == (False, None)
