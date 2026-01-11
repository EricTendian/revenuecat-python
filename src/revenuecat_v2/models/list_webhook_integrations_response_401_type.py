from enum import Enum


class ListWebhookIntegrationsResponse401Type(str, Enum):
    AUTHENTICATION_ERROR = "authentication_error"

    def __str__(self) -> str:
        return str(self.value)
