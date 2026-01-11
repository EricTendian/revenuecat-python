from enum import Enum


class WebhookIntegrationEnvironmentType1(str, Enum):
    PRODUCTION = "production"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
