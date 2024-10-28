from sqlmodel import create_engine, SQLModel, Session
from db.config import settings

engine = create_engine(settings.DATABASE_URL, echo=False)  # No echo to prevent logging of SQL queries

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)