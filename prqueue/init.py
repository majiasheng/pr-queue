from persistence import entities
from sqlalchemy.engine import Engine

def init_app(engine: Engine) -> None:
    '''
    - set up db (if not already done so)
    - configure logger
    '''
    if (not entities.PrQueue.exists(engine)):
        entities.pr_queue_meta_data.create_all(engine)
