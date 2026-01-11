from enum import Enum


class PublicApiKeyObject(str, Enum):
    PUBLIC_API_KEY = "public_api_key"

    def __str__(self) -> str:
        return str(self.value)
