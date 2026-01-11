from enum import Enum


class PublicApiKeyEnvironment(str, Enum):
    PRODUCTION = "production"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
