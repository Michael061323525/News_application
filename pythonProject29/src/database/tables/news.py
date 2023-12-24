from src.database.tables.base import BaseModel
from sqlalchemy import Integer, Column, Text


class News(BaseModel):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    news_id = Column(Integer)
    author = Column(Text)
    title = Column(Text)
    url = Column(Text)