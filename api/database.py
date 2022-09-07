# 3rd-party Dependencies
# ----------------------
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB URL (for SQLite it is the file path)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_api.db"

# DB engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # only for SQLite
)

# DB session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base SQLAlchemy model
Base = declarative_base()
