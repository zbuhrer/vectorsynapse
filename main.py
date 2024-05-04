import flet as ft
from src import vector_talk

class VectorSynapse(ft.Column):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.text_field = ft.TextField(label='Vector speak...')
        self.submit_button = ft.ElevatedButton("Say", on_click=self.send)
        self.messages_widget = ft.ListView()
        self.text_field.value = ""
        self.messages_list = []
        self.controls = [
            self.text_field,
            self.submit_button,
            self.messages_widget,
        ]

    async def send(self, text):
        text = str(self.text_field.value)
        await vector_talk.talk(text)
        self.messages_widget.controls.append(ft.Text(text))
        self.text_field.value = ""
        self.update()

def main(page: ft.Page):
    page.title = "Vector Synapse"
    page.add(
        VectorSynapse(),
        )

if __name__ == "__main__":
    ft.app(main)