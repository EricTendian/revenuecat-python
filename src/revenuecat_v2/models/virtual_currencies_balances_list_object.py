from enum import Enum


class VirtualCurrenciesBalancesListObject(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
