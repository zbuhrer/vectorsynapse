import flet as ft
from src import vector_talk
import asyncio 

from flet import margin

class Chat(ft.Column):
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
            self.messages_widget
            ]

    async def send(self, text):
        text = str(self.text_field.value)
        self.text_field.disabled = True
        self.submit_button.disabled = True
        self.update()

        try: 
            await vector_talk.talk(text)
            self.messages_widget.controls.append(ft.Text(text))
            self.update()
        except asyncio.TimeoutError as e:
            print(f"Timeout error: {e}")
            self.messages_list.append(e)
            self.update()
            pass

        self.text_field.disabled = False
        self.submit_button.disabled = False
        self.text_field.value = ""
        self.update()