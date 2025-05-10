from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    ARRAY
)

from databases import Database

DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/reports_db'

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

metadata = MetaData()

reports = Table(
    "reports",
    metadata,
    Column("id", String, primary_key=True),
    Column("content", ARRAY(String)),
    Column("status", String),
    Column("created_at", String),
    Column("updated_at", String),
    Column("user_id", Integer)
)
