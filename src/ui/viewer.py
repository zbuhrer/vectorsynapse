from flet import Page, Tabs, Tab, Container, Margin

from src.ui.chat import Chat
from src.ui.settings import Settings
from src.ui.about import About
from src.ui.status import Status

class MainView(Page):
    def __init__(self):

        # Tab content 
        self.status_content = Container(Status(), padding=10)
        self.chat_content = Container(Chat(),padding=10)
        self.settings_content = Container(Settings(),padding=10)
        self.about_content = Container(About(),padding=10)

        # Tabs
        self.tab_status = Tab(text='Status',content=self.status_content)
        self.tab_chat = Tab(text='Chat',content=self.chat_content)
        self.tab_settings = Tab(text='Settings',content=self.settings_content)
        self.tab_about = Tab(text='About',content=self.about_content)
        self.tabs = Tabs(
            tabs=[
                self.tab_status,
                self.tab_chat, 
                self.tab_settings, 
                self.tab_about
            ]
        )