from sqlalchemy import inspect
import os
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
from dotenv import load_dotenv

from databases import Database

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

people = Table(
    'people',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', String, foreign_key='users.id'),
    Column('name', String(50)),
    Column('created_at', String(50)),
    Column('updated_at', String(50)),
)

database = Database(DATABASE_URL)


async def create_database():
    if not database.is_connected:
        await database.connect()
    print("Checking if database exists...")
    query = "SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='people')"
    result = await database.fetch_one(query=query)
    if not result[0]:
        print("Creating database...")
        query = """
        CREATE TABLE people (
            id SERIAL PRIMARY KEY,
            user_id VARCHAR(50) REFERENCES users(id),
            name VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        await database.execute(query=query)
        query = "CREATE INDEX idx_user_id ON people (user_id)"
        await database.execute(query=query)
        query = "CREATE INDEX idx_people_id ON people (id)"
        await database.execute(query=query)
        print("Database created.")
    else:
        print("Database already exists.")
    print("Database check complete.")
