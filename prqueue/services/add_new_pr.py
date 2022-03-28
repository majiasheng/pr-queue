from app import db_engine
from classes.pull_request import PullRequest
from persistence import db_manager


def add_new_pr(pr: PullRequest) -> str:
    res = db_manager.add_new_pr(db_engine, pr)
    id = res.inserted_primary_key[0]
    return id
