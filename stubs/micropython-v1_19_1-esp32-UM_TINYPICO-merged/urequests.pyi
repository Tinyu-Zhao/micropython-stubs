from typing import Any

def get(*args, **kwargs) -> Any: ...
def put(*args, **kwargs) -> Any: ...

class Response:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    text: Any
    def json(self, *args, **kwargs) -> Any: ...
    content: Any

def request(*args, **kwargs) -> Any: ...
def head(*args, **kwargs) -> Any: ...
def post(*args, **kwargs) -> Any: ...
def patch(*args, **kwargs) -> Any: ...
def delete(*args, **kwargs) -> Any: ...
