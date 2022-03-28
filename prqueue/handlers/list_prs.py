import services
from classes.pull_request import PullRequest
from typing import Dict, Any, List
from  constants.request import DEFAULT_PAGE_SIZE


def list_prs(request_args: Dict[str, Any]) -> List[PullRequest]:
    try:
        page = int(request_args.get('page', 1))
        limit = int(request_args.get('limit', DEFAULT_PAGE_SIZE))
    except ValueError as ve:
        page = 1
        limit = DEFAULT_PAGE_SIZE

    # page has to be greater than 0
    page = max(page, 1)
    offset = (page-1) * limit


    return services.list_prs(limit, offset)
