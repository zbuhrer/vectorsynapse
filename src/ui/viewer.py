from pydoc import pager
from flet import Page, Column, View, Card, Tabs, Tab, Container
from flet import NavigationRail, NavigationRailDestination, NavigationRailLabelType, NavigationRailTheme

from src.ui.chat import Chat
from src.ui.settings import Settings
from src.ui.about import About

class MainView(Page):
    def __init__(self):

        # Tab content 
        self.chat_content = Container(Chat())
        self.settings_content = Container(Settings())
        self.about_content = Container(About())

        # Tabs
        self.tab_chat = Tab(text='Chat',content=self.chat_content)
        self.tab_settings = Tab(text='Settings',content=self.settings_content)
        self.tab_about = Tab(text='About',content=self.about_content)
        self.tabs = Tabs(
            tabs=[
                self.tab_chat, 
                self.tab_settings, 
                self.tab_about
            ]
        )