from enum import Enum


class ListCustomerInvoicesResponse403Type(str, Enum):
    AUTHORIZATION_ERROR = "authorization_error"

    def __str__(self) -> str:
        return str(self.value)
