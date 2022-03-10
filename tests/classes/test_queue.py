from prqueue.classes.complexity import Complexity
from prqueue.classes.importance import Importance
from prqueue.classes.queue import Queue
from prqueue.classes.pull_request import PullRequest
from prqueue.classes.urgency import Urgency
import unittest


class TestEmptyQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.pr_queue = Queue()

    def test_enqueue(self) -> None:
        pr = PullRequest(
            'https://github.com/majiasheng/majiasheng-vue/pull/22',
            urgency=Urgency.URGENT,
            importance=Importance.IMPORTANT)
        self.pr_queue.enqueue(pr)

        self.assertEqual(self.pr_queue.peek().link, pr.link)

    def test_peek(self) -> None:
        self.assertIsNone(self.pr_queue.peek())

    def test_dequeue(self) -> None:
        self.assertIsNone(self.pr_queue.dequeue())

    def test_len(self) -> None:
        self.assertEqual(len(self.pr_queue), 0)


class TestPopulatedQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.pr_queue = Queue()

        self.pr1 = PullRequest(
            'https://github.com/majiasheng/majiasheng-vue/pull/21',
            urgency=Urgency.URGENT,
            importance=Importance.IMPORTANT)

        self.pr2 = PullRequest(
            'https://github.com/majiasheng/majiasheng-vue/pull/22',
            urgency=Urgency.URGENT,
            importance=Importance.NOT_AS_IMPORTANT)

        self.pr_queue.enqueue(self.pr1)
        self.pr_queue.enqueue(self.pr2)

    def test_len(self):
        self.assertEqual(len(self.pr_queue), 2)

    def test_enqueue(self) -> None:
        pr = PullRequest(
            'https://github.com/majiasheng/majiasheng-vue/pull/23',
            urgency=Urgency.URGENT,
            importance=Importance.IMPORTANT,
            complexity=Complexity.NOT_AS_COMPLEX)
        self.pr_queue.enqueue(pr)

        self.assertEqual(len(self.pr_queue), 3)
        self.assertEqual(self.pr_queue.peek().link, pr.link)

    def test_peek(self) -> None:
        first_pr = self.pr_queue.peek()
        self.assertIsNotNone(first_pr)
        self.assertEqual(first_pr, self.pr1)

    def test_dequeue(self) -> None:
        pr = self.pr_queue.dequeue()
        self.assertIsNotNone(pr)
        self.assertEqual(pr, self.pr1)
        self.assertEqual(len(self.pr_queue), 1)


if __name__ == '__main__':
    unittest.main()
