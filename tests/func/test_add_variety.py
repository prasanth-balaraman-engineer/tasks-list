import pytest
import tasks
from tasks import Task

tasks_to_try = (Task("Sleep", "brian", True),
                Task("Eat", "brian"),
                Task("Wake", "prasanth", False),
                Task("Exercise", "test", True))
task_ids = ["Task({}, {}, {})".format(t.summary, t.owner, t.done) for t in tasks_to_try]

task_args_to_try = (("Sleep", "brian", True),
                    ("Eat", "brian", True),
                    ("Wake", "prasanth", False),
                    ("Exercise", "test", True))


@pytest.mark.parametrize("task", tasks_to_try, ids=task_ids)
def test_add_1(task, initialized_db):
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)
    assert equivalence(task, task_from_db)


@pytest.mark.parametrize("summary, owner, done", task_args_to_try)
def test_add_2(summary, owner, done, initialized_db):
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)
    assert equivalence(task, task_from_db)


def equivalence(t1, t2):
    return (
            (t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done)
    )
