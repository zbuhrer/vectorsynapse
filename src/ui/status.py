from flet import Container, Text
from src.vector_init import Synapse

class Status(Container):
    botdata = Synapse.loadbot
    
    def __init__(self):
        super().__init__()
        self.contents = [
            Text("Status"),
            Text(f"Current Bot: {self.botdata}")
            ]