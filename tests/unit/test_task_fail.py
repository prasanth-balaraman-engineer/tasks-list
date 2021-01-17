from tasks import Task


def test_task_equality():
    t1 = Task("sit there", "brian")
    t2 = Task("do something", "okken")
    assert t1 != t2


def test_dict_equality():
    t1_dict = Task("do something", "okken")._asdict()
    t2_dict = Task("do something", "okkem")._asdict()
    assert t1_dict != t2_dict
