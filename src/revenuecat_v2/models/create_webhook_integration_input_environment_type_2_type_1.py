from enum import Enum


class CreateWebhookIntegrationInputEnvironmentType2Type1(str, Enum):
    PRODUCTION = "production"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
