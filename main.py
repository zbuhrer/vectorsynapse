import flet as ft

from src.ui.viewer import MainView
from src.vector_init import Synapse


def main(page: ft.Page):
    def __init__(self):
        self.page.title = "Vector Synapse"

    mv = MainView()
    page.add(mv.tabs)

if __name__ == "__main__":
    ft.app(main)