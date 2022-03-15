from app import db_engine
from persistence import db_manager
from classes.pull_request import PullRequest


def peek() -> PullRequest:
    _prs = db_manager.peek(db_engine).mappings().all()

    if len(_prs) == 0:
        return None

    prs = list(
        map(lambda pr: db_manager.create_pr_from_db_record(pr).to_json(), _prs))

    return prs
