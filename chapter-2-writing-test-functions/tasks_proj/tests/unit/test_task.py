from tasks_proj.tasks import Task


def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task(summary='do something', owner='Okken', done=True, id=21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something', 'owner': 'Okken', 'done': True, 'id': 21}

    assert t_dict == expected


def test_replace():
    """replace() should change passed in fields."""
    task_before = Task(summary='finish book', owner='Brian', done=False)
    task_after = task_before._replace(id=10, done=True)
    task_expected = Task(summary='finish book', owner='Brian', done=True, id=10)

    assert task_after == task_expected


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)

    assert t1 == t2


def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task(summary='buy milk', owner='Brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'Brian'
    assert (t.done, t.id) == (False, None)
