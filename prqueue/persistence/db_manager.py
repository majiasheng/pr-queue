import constants.prqueue as c
import sqlalchemy as sa
import uuid

from classes.pull_request import PullRequest
from . import config
from . import secrets
from . import entities


def get_engine() -> sa.engine.Engine:
    # TODO : set up db
    return sa.create_engine(
        f"postgresql://{config.sql_user}:{secrets.sql_password}@{config.sql_host}:{config.sql_port}/{config.sql_database}"
    )


def get_sqlite_engine() -> sa.engine.Engine:
    return sa.create_engine("sqlite:///.sqlite.db", echo=True)


def close_pr(engine: sa.engine.Engine, link: str) -> sa.engine.ResultProxy:
    pass


def add_new_pr(engine: sa.engine.Engine, pr: PullRequest) -> sa.engine.ResultProxy:
    insert_statement = entities.PrQueue.insert().values(
        {
            c.ID: str(uuid.uuid4()),
            c.LINK: pr.link,
            c.PRIORITY: pr.get_priority()
        }
    )
    return engine.execute(insert_statement)


def list_prs(engine: sa.engine.Engine, limit: int = 10, offset: int = 0) -> sa.engine.ResultProxy:
    select_statement = entities.PrQueue.select().limit(limit).offset(offset)
    return engine.execute(select_statement)
