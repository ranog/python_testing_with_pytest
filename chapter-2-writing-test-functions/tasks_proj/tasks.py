from collections import namedtuple

Task = namedtuple(typename='Task', field_names=['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)
