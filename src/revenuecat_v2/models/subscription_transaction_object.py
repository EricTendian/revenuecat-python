from enum import Enum


class SubscriptionTransactionObject(str, Enum):
    SUBSCRIPTION_TRANSACTION = "subscription_transaction"

    def __str__(self) -> str:
        return str(self.value)
