from sqlalchemy import (
    Column,
    MetaData,
    String,
    Table,
    create_engine
)

from databases import Database

DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/postgres'

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", String, primary_key=True),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("created_at", String),
    Column("updated_at", String),
)
