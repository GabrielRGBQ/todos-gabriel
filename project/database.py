from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# We connect to a SQL database by opening a file with a SQL database (./sql_app.db).
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo_app.db"

# We need to create a SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# We create a SessionLocal class, whose instances will be database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This will be used to create the SQLAlchemy models in models.py
Base = declarative_base()
