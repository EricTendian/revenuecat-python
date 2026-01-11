from enum import Enum


class UpdateWebhookIntegrationResponse503Type(str, Enum):
    SERVER_ERROR = "server_error"

    def __str__(self) -> str:
        return str(self.value)
