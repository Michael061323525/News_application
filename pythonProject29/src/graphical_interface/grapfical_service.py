import customtkinter as ctk
from src.settings.tasks import task_load_database
from src.external_data.hacker_news import HackerNewsService
from src.graphical_interface.custom_app import App


class Screen:

    def __init__(self):
        self.hacker_service = HackerNewsService()

    def run_main_window(self):
        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        app = App()  # create CTk window like you do with the Tk window
        app.geometry("400x600")

        button = ctk.CTkButton(master=app, text="Загрузить данные", command=self.put_news_button)
        button.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

        all_titles = self.hacker_service.get_all_titles_from_database()
        for title in all_titles:
            text_1 = ctk.CTkTextbox(master=app, width=300, height=50)
            text_1.pack()
            text_1.insert("0.0", title)
            text_1.configure(state=ctk.DISABLED)

        app.mainloop()

    def put_news_button(self):
        task_load_database()
