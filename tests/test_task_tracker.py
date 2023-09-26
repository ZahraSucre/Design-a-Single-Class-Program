import pytest
from lib.task_tracker import TaskTracker

"""
Initially, there are no tasks
"""
def test_initially_has_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []

"""
When we add a task
It is reflected in the list of tasks
"""
def test_add_task_reflected_in_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    assert tracker.list_incomplete() == ["Walk the dog"]

"""
When we add multiple tasks
They all reflected in the list of tasks
"""
def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the lion")
    assert tracker.list_incomplete() == [
        "Walk the dog", "Walk the cat", "Walk the lion"]

"""
When we add multiple tasks
And mark one as complete
It disappears from the task list
"""
def test_marks_tasks_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the lion")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ["Walk the dog", "Walk the lion"]

"""
If we try to mark a tracker complete that does not exist (too low)
It raises an error
"""
def test_mark_task_that_is_too_low_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(-1)
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]

"""
If we try to mark a tracker complete that does not exist (too high)
It raises an error
"""
def test_mark_task_that_is_too_high_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(1)
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]
