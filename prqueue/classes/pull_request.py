from enum import Enum
from .urgency import Urgency
from .importance import Importance
from .complexity import Complexity
from .priority import Priority


class Status(Enum):
    OPEN = 'OPEN'
    IN_REVIEW = 'IN_REVIEW'
    CLOSE = 'CLOSED'


class PullRequest(Priority):

    def __init__(self, link: str, status: Status = Status.OPEN, urgency: Urgency = Urgency.DEFAULT, importance: Importance = Importance.DEFAULT, complexity: Complexity = Complexity.DEFAULT) -> None:
        self.link = link
        self.status = status
        super().__init__(urgency, importance, complexity)
