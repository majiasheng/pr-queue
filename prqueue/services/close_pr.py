from app import db_engine
from persistence import db_manager

def close_pr(link: str) -> bool:
    res = db_manager.close_pr(db_engine, link)
    if res.rowcount > 0:
        return True
    return False
