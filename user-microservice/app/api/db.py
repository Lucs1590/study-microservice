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


async def create_database():
    if not database.is_connected:
        await database.connect()
    print("Checking if database exists...")
    query = "SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='users')"
    result = await database.fetch_one(query=query)
    if not result[0]:
        print("Creating database...")
        query = "CREATE TABLE users (id VARCHAR(50) PRIMARY KEY, email VARCHAR(50), password VARCHAR(50), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        await database.execute(query=query)
        query = "CREATE INDEX idx_email ON users (email)"
        await database.execute(query=query)
        query = "CREATE INDEX idx_user_id ON users (id)"
        await database.execute(query=query)
        print("Database created.")
    else:
        print("Database already exists.")
    print("Database check complete.")
