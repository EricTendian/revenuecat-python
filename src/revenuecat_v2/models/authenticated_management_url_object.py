from enum import Enum


class AuthenticatedManagementUrlObject(str, Enum):
    AUTHENTICATED_MANAGEMENT_URL = "authenticated_management_url"

    def __str__(self) -> str:
        return str(self.value)
