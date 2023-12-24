from src.external_data.interface import ExternalServiceInterface
import requests
from src.external_data.exception import NotExternalConnectException
from src.database.tables.news import News
from src.external_data.repository import NewsRepository
import logging
from logging import config
from src.settings.app import BASIC_URL_NEWS
from src.settings.app import COUNT_OF_NEWS
from src.settings.app import LOG_CONFIG


config.dictConfig(LOG_CONFIG)


class HackerNewsService(ExternalServiceInterface):

    def __init__(self):
        self.basic_url = BASIC_URL_NEWS
        self.news_data = []
        self.news_repository = NewsRepository()

    def get_data(self):
        try:
            top_ids_response = requests.get(f"{self.basic_url}topstories.json")
            return top_ids_response.json()
        except requests.exceptions.ConnectionError:
            raise NotExternalConnectException("Нет соединения с Hacker-News", -1)

    def get_news(self):
        ids = self.get_data()
        for news_id in ids[:COUNT_OF_NEWS]:
            try:
                news = self.news_repository.exist_news(news_id)
                if news is None:
                    news_response = requests.get(f"{self.basic_url}item/{news_id}.json")
                    news_data = news_response.json()
                    self.news_data.append(News(news_id=news_data['id'], author=news_data["by"],
                                        title=news_data["title"], url=news_data["url"]))
                    logging.info(f"Добавляется строка с заголовком {news_data['title']}")
            except requests.exceptions.ConnectionError:
                logging.error("Нет соединение с Hacker-News")
            except KeyError:
                logging.info(f"Новость с id = {news_id} некорректна")
                continue

    def put_news_in_database(self):
        self.get_news()
        self.news_repository.put_news(self.news_data)

    def get_all_titles_from_database(self):
        return self.news_repository.get_all_titles()


