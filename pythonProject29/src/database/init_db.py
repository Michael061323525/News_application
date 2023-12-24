from sqlalchemy import create_engine
from src.database.tables.base import BaseModel


sqlite_database = "sqlite:///metanit.db"
engine = create_engine(sqlite_database)
BaseModel.metadata.create_all(bind=engine)
