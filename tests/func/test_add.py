"""
Placeholder test file.

We'll add a bunch of tests here in later versions.
"""
import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id(initialized_db):
    new_task = Task("do something")
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set(initialized_db):
    new_task = Task("do something")
    task_id = tasks.add(new_task)

    fetched_task = tasks.get(task_id)
    assert fetched_task.id == task_id


def test_add_increase_count(db_with_3_tasks):
    tasks.add(Task("do something"))
    assert tasks.count() == 4
