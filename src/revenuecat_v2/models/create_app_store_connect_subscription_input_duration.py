from enum import Enum


class CreateAppStoreConnectSubscriptionInputDuration(str, Enum):
    ONE_MONTH = "ONE_MONTH"
    ONE_WEEK = "ONE_WEEK"
    ONE_YEAR = "ONE_YEAR"
    SIX_MONTHS = "SIX_MONTHS"
    THREE_MONTHS = "THREE_MONTHS"
    TWO_MONTHS = "TWO_MONTHS"

    def __str__(self) -> str:
        return str(self.value)
