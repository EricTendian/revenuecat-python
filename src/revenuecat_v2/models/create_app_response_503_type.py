from enum import Enum


class CreateAppResponse503Type(str, Enum):
    SERVER_ERROR = "server_error"

    def __str__(self) -> str:
        return str(self.value)
