from enum import Enum


class PaywallObject(str, Enum):
    PAYWALL = "paywall"

    def __str__(self) -> str:
        return str(self.value)
