import flet as ft
from src.ui.viewer import MainView


def main(page: ft.Page):
    page.title = "Vector Synapse"
    mv = MainView()

    page.add(mv.tabs)

if __name__ == "__main__":
    ft.app(main)