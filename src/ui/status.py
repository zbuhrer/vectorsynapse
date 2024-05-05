from flet import Container, Text

class Status(Container):
    def __init__(self):
        super().__init__()
        self.contents = [
            Text("Status")
            ]