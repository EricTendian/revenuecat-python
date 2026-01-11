from enum import Enum


class CreateWebhookIntegrationInputEnvironmentType3Type1(str, Enum):
    PRODUCTION = "production"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
