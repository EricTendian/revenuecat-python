from enum import Enum


class ListCustomersResponse404Type(str, Enum):
    RESOURCE_MISSING = "resource_missing"

    def __str__(self) -> str:
        return str(self.value)
