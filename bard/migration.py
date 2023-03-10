import flask_migrate
from sqlalchemy import MetaData, inspect
from sqlalchemy.exc import InternalError
from sqlalchemy.dialects.postgresql import ENUM
from bard.app import db

def upgrade_system():
    flask_migrate.upgrade()




def destroy_db():
    metadata = MetaData()
    metadata.bind = db.engine
    metadata.reflect()
    tables = list(metadata.sorted_tables)
    while len(tables):
        for table in tables:
            try:
                table.drop(checkfirst=True)
                tables.remove(table)
            except InternalError:
                pass
    for enum in inspect(db.engine).get_enums():
        enum = ENUM(name=enum["name"])
        enum.drop(bind=db.engine, checkfirst=True)

