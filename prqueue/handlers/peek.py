import services
from classes.pull_request import PullRequest


def peek() -> PullRequest:
    return services.peek()
