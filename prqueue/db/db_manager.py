import sqlalchemy as sa
from . import config
from . import secrets

def get_engine() -> sa.engine.Engine:
    # TODO : set up db
    return sa.create_engine(
        f"postgresql://{config.sql_user}:{secrets.sql_password}@{config.sql_host}:{config.sql_port}/{config.sql_database}"
    )

def get_sqlite_engine():
    return sa.create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
