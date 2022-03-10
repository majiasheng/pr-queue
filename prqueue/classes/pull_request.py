from .urgency import Urgency
from .importance import Importance
from .complexity import Complexity
from .priority import Priority


class PullRequest(Priority):

    def __init__(self, link: str, urgency: Urgency = Urgency.DEFAULT, importance: Importance = Importance.DEFAULT, complexity: Complexity = Complexity.DEFAULT) -> None:
        self.link = link
        super().__init__(urgency, importance, complexity)
