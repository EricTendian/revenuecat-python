from enum import Enum


class Duration(str, Enum):
    P1M = "P1M"
    P1W = "P1W"
    P1Y = "P1Y"
    P2M = "P2M"
    P3M = "P3M"
    P6M = "P6M"

    def __str__(self) -> str:
        return str(self.value)
