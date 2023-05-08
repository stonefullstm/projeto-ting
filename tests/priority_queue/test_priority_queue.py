import pytest
from ting_file_management.priority_queue import PriorityQueue


file1 = {"qtd_linhas": 10}
file2 = {"qtd_linhas": 12}
file3 = {"qtd_linhas": 8}
file4 = {"qtd_linhas": 3}
file5 = {"qtd_linhas": 4}


def test_basic_priority_queueing():
    priorityQueue = PriorityQueue()
    priorityQueue.enqueue(file1)
    priorityQueue.enqueue(file2)
    priorityQueue.enqueue(file3)

    assert priorityQueue.dequeue() == file1
    priorityQueue.enqueue(file4)
    priorityQueue.enqueue(file5)
    assert priorityQueue.dequeue() == file4
    assert priorityQueue.search(len(priorityQueue) - 1) == file3
    with pytest.raises(IndexError):
        priorityQueue.search(10)
