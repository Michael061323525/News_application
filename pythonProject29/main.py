from src.external_data.hacker_news import HackerNewsService
import os
from src.graphical_interface.grapfical_service import Screen

if __name__ == "__main__":
    value = int(os.getenv("INIT_DB"))
    if value:
        hacker_news_object = HackerNewsService()
        hacker_news_object.put_news_in_database()
    graphical_service_object = Screen()
    graphical_service_object.run_main_window()

