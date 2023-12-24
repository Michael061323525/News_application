from sqlalchemy.orm import Session
from src.database.init_db import engine
from sqlalchemy import select
from src.database.tables import News


class NewsRepository:

    def put_news(self, news_data):
        with Session(engine) as session:
            session.add_all(news_data)
            session.commit()

    def get_all_titles(self):
        stmt = select(News.title)
        with Session(engine) as session:
            result = session.execute(stmt)
            result = result.scalars().all()
            return result

    def exist_news(self, news_id):
        stmt = select(News).where(News.news_id == news_id)
        with Session(engine) as session:
            result = session.execute(stmt)
            result = result.scalar_one_or_none()
            return result