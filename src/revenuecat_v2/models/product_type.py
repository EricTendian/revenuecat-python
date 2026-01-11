from enum import Enum


class ProductType(str, Enum):
    CONSUMABLE = "consumable"
    NON_CONSUMABLE = "non_consumable"
    NON_RENEWING_SUBSCRIPTION = "non_renewing_subscription"
    ONE_TIME = "one_time"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
