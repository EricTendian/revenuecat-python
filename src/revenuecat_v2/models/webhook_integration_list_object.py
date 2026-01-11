from enum import Enum


class WebhookIntegrationListObject(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
