from enum import Enum


class ListPurchaseEntitlementsResponse423Type(str, Enum):
    RESOURCE_LOCKED_ERROR = "resource_locked_error"

    def __str__(self) -> str:
        return str(self.value)
