import services
from classes.urgency import Urgency
from classes.importance import Importance
from classes.complexity import Complexity
from classes.pull_request import PullRequest
from typing import Any, Dict, Union


class MissingLinkException(Exception):
    def __init__(self) -> None:
        msg = '"link" is missing from request'
        super().__init__(msg)


class BadPriorityAttributeException(Exception):
    def __init__(self) -> None:
        msg = 'urgency/importance/complexity can only be 0 or 1'
        super().__init__(msg)


def add_new_pr(request_data: Dict[str, Any]) -> str:
    # validate and create PullRequest object
    link = request_data.get('link', None)
    urgency = get_priority_attr_from_request(request_data, Urgency)
    importance = get_priority_attr_from_request(request_data, Importance)
    complexity = get_priority_attr_from_request(request_data, Complexity)

    if link is None:
        raise MissingLinkException()

    if None in (urgency, importance, complexity):
        raise BadPriorityAttributeException()

    pr = PullRequest(
        link,
        urgency=urgency,
        importance=importance,
        complexity=complexity
    )
    id = services.add_new_pr(pr)

    return id


def get_priority_attr_from_request(request_data: Dict[str, Any], priority_attr: Union[Urgency, Importance, Complexity]) -> Union[Urgency, Importance, Complexity]:
    _p = None
    if priority_attr == Urgency:
        _p = request_data.get('urgency', None)
    elif priority_attr == Importance:
        _p = request_data.get('importance', None)
    elif priority_attr == Complexity:
        _p = request_data.get('complexity', None)

    if _p is None:
        return priority_attr.DEFAULT

    if type(_p) == int:
        p = priority_attr(
            min(
                max(_p, 0),  # positive integer only
                priority_attr.DEFAULT.value
            )  # number can only go as high as default
        )

        return p
    else:
        return None
