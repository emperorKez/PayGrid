from typing import Generator
from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///./payments.db"
engine = create_engine(DATABASE_URL, echo=True)

def get_db_session() -> Generator[Session, None, None]:
    """
    Dependency to get a database session.
    """
    with Session(engine) as session:
        yield session

# You might want a function to create the DB tables for the first run
def create_db_and_tables():
    from src.payments.models import SQLModel
    SQLModel.metadata.create_all(engine)

# Call this on app startup
create_db_and_tables()
