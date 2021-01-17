import pytest
import tasks


def test_add_raises():
    with pytest.raises(TypeError):
        tasks.add(task='not a task')


def test_start_tasks_db_raises():
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db("some/great/path", "mysql")

    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_raises():
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    with pytest.raises(TypeError):
        tasks.get(id='not an integer')


class TestUpdate():
    def test_bad_id(self):
        with pytest.raises(TypeError):
            tasks.update(task_id={"dict instead": 1})
    
    def test_bad_task(self):
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task="not a task")

