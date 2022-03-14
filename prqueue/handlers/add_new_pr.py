import services
from classes.pull_request import PullRequest
from typing import Any, Dict


def add_new_pr(data: Dict[str, Any]) -> str:
    # validate and create PullRequest object
    link = data.get('link', None)
    # link = data.get('link', None)
    # link = data.get('link', None)
    # link = data.get('link', None)
    # link = data.get('link', None)
    if link is None:
        return
    try:
        # TODO: use other fields for instantiation
        pr = PullRequest(link)
        id = services.add_new_pr(pr)
        # TODO: create response object
        return id
    except Exception as e:
        # TODO: return error
        import traceback
        traceback.print_exc()
        return {'error': str(e)}
