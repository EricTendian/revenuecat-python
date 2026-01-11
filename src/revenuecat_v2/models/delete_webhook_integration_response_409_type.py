from enum import Enum


class DeleteWebhookIntegrationResponse409Type(str, Enum):
    IDEMPOTENCY_ERROR = "idempotency_error"
    RESOURCE_ALREADY_EXISTS = "resource_already_exists"

    def __str__(self) -> str:
        return str(self.value)
