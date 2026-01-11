from enum import Enum


class CreatePackagesResponse403Type(str, Enum):
    AUTHORIZATION_ERROR = "authorization_error"

    def __str__(self) -> str:
        return str(self.value)
