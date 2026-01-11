from enum import Enum


class ListWebhookIntegrationsResponse429Type(str, Enum):
    RATE_LIMIT_ERROR = "rate_limit_error"

    def __str__(self) -> str:
        return str(self.value)
