import services
from classes.pull_request import PullRequest
from  constants.request import DEFAULT_PAGE_SIZE


def peek() -> PullRequest:
    return services.peek()
