import pytest
import tasks
from tasks import Task


@pytest.mark.xfail(tasks.__version__ < '0.2.0', reason="misunderstood the API")
def test_unique_id_1(initialized_db):
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2


@pytest.mark.xfail()
def test_unique_id_is_duck(initialized_db):
    uid = tasks.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_is_not_duck(initialized_db):
    uid = tasks.unique_id()
    assert uid != 'a duck'


def test_unique_id_2(initialized_db):
    ids = [tasks.add(Task("One")), tasks.add(Task("Two")), tasks.add(Task("Three"))]

    uid = tasks.unique_id()
    assert uid not in ids
