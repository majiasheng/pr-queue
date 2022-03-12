from typing import Any, Dict
from app import db_engine
from persistence import db_manager
from classes.pull_request import PullRequest
from constants.request import DEFAULT_PAGE_SIZE

def _create_pr_from_db_record(pr: Dict[str, Any]) -> PullRequest:
    priority = PullRequest.decode_prority(pr['priority'])
    return PullRequest(
        pr['link'],
        urgency=priority['urgency'],
        importance=priority['importance'],
        complexity=priority['complexity']
    )

def list_prs(limit: int=DEFAULT_PAGE_SIZE, offset: int=0) -> Dict[str, Any]:
    _prs = db_manager.list_prs(db_engine, limit, offset).mappings().all()
    prs = list(map(lambda pr: _create_pr_from_db_record(pr).to_json(), _prs))

    return prs