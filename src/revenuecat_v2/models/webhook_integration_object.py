from enum import Enum


class WebhookIntegrationObject(str, Enum):
    WEBHOOK_INTEGRATION = "webhook_integration"

    def __str__(self) -> str:
        return str(self.value)
