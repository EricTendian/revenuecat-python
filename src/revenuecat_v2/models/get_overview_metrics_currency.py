from enum import Enum


class GetOverviewMetricsCurrency(str, Enum):
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    CNY = "CNY"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    KRW = "KRW"
    MXN = "MXN"
    PLN = "PLN"
    SEK = "SEK"
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
