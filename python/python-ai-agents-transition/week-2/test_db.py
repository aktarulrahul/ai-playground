# type: ignore
import os
from dotenv import load_dotenv
import sqlalchemy
from databases import Database

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Use PostgreSQL for testing (same as production)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

TEST_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

test_database = Database(TEST_DATABASE_URL)
test_metadata = sqlalchemy.MetaData()

test_teas = sqlalchemy.Table(
    "teas",
    test_metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True),
)

# Create tables for testing
test_engine = sqlalchemy.create_engine(
    TEST_DATABASE_URL.replace("+asyncpg", ""),  # Use sync driver for schema creation
)
test_metadata.create_all(test_engine) 