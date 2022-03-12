from enum import Enum
from typing import Any, Dict
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

    def to_json(self) -> Dict[str, Any]:
        return {
            'link': self.link,
            'priority': {
                'level': self.get_priority(),
                'urgency': self.urgency.name,
                'importance': self.importance.name,
                'complexity': self.complexity.name
            }
        }
