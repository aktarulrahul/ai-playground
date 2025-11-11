import os
from dotenv import load_dotenv
import sqlalchemy
from databases import Database

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.', '.env')
print(f"Loading environment variables from: {dotenv_path}")
load_dotenv(dotenv_path=dotenv_path)

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

print(f"POSTGRES_USER: {POSTGRES_USER}")
print(f"POSTGRES_PASSWORD: {'*' * len(POSTGRES_PASSWORD) if POSTGRES_PASSWORD else None}")
print(f"POSTGRES_DB: {POSTGRES_DB}")
print(f"POSTGRES_HOST: {POSTGRES_HOST}")
print(f"POSTGRES_PORT: {POSTGRES_PORT}")

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Mask password in log
masked_url = DATABASE_URL.replace(f":{POSTGRES_PASSWORD}@", ":****@") if POSTGRES_PASSWORD else DATABASE_URL
print(f"Using DATABASE_URL: {masked_url}")

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

teas = sqlalchemy.Table(
    "teas",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True),
)

print("Creating tables if they do not exist...")
# Use SQLAlchemy's engine for schema creation (sync driver)
engine = sqlalchemy.create_engine(
    DATABASE_URL.replace("+asyncpg", ""),  # Use sync driver for schema creation
)
metadata.create_all(engine)
print("Tables created (if not already present).")