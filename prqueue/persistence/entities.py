import sqlalchemy as sa
import constants.prqueue as c

pr_queue_meta_data = sa.schema.MetaData()

PrQueue = sa.schema.Table(
    'prqueue',
    pr_queue_meta_data,
    sa.schema.Column(c.ID, sa.types.String, primary_key=True),
    sa.schema.Column(c.LINK, sa.types.String, nullable=False, unique=True),
    sa.schema.Column(c.PRIORITY, sa.types.SMALLINT, nullable=False),
    sa.schema.Column(c.DATE_CREATED, sa.types.DateTime, nullable=False, default=sa.sql.func.now()),
    sa.schema.Column(c.DATE_UPDATED, sa.types.DateTime, nullable=False, default=sa.sql.func.now())
)
