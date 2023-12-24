from celery import Celery
from src.external_data.hacker_news import HackerNewsService

app = Celery('tasks', broker_url='redis://127.0.0.1:6379/0')


# @app.task
def task_load_database():
    hacker_service = HackerNewsService()
    hacker_service.put_news_in_database()
