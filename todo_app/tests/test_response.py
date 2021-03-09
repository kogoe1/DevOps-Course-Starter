import json

class MockedResponse:

    def __init__(self, value) -> None:
        self.value = value

    def json(self):
        return self.value