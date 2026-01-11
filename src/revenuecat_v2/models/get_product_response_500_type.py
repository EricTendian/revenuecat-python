from enum import Enum


class GetProductResponse500Type(str, Enum):
    SERVER_ERROR = "server_error"

    def __str__(self) -> str:
        return str(self.value)
