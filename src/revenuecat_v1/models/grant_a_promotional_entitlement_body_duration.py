from enum import Enum


class GrantAPromotionalEntitlementBodyDuration(str, Enum):
    DAILY = "daily"
    LIFETIME = "lifetime"
    MONTHLY = "monthly"
    SIX_MONTH = "six_month"
    THREE_DAY = "three_day"
    THREE_MONTH = "three_month"
    TWO_MONTH = "two_month"
    TWO_WEEK = "two_week"
    WEEKLY = "weekly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
