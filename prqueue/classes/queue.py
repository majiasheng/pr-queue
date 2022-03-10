from .priority import Priority, priority_matrix
from .urgency import Urgency
from .importance import Importance
from .complexity import Complexity
from functools import reduce

'''
priority queue
'''


class Queue:
    # TODO: need to implement strategy to avoid starvation

    # urgency > importance > complexity
    def __init__(self) -> None:
        self.queue = [[] for i in range(len(priority_matrix))]

    def peek(self) -> Priority:
        for pq in self.queue:
            if len(pq):
                return pq.pop(0)

        return None

    def enqueue(self, data: Priority) -> None:
        priority = data.get_priority()
        self.queue[priority].append(data)

    def dequeue(self) -> None:
        '''
        Remove the first item in the first available queue
        '''
        for pq in self.queue:
            if len(pq):
                return pq.pop(0)

        return None

    def dequeue_(self) -> None:
        # TODO:
        pass

    def __len__(self) -> int:
        return reduce(lambda a, b: a+b, [len(q) for q in self.queue])
