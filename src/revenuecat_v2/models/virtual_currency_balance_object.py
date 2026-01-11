from enum import Enum


class VirtualCurrencyBalanceObject(str, Enum):
    VIRTUAL_CURRENCY_BALANCE = "virtual_currency_balance"

    def __str__(self) -> str:
        return str(self.value)
