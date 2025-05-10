import os
from sqlalchemy import (
    Column,
    MetaData,
    String,
    Table,
    create_engine
)

from databases import Database

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", String, primary_key=True),
    Column("email", String(50), nullable=False),
    Column("password", String(50), nullable=False),
    Column("created_at", String),
    Column("updated_at", String),
)

database = Database(DATABASE_URL)
