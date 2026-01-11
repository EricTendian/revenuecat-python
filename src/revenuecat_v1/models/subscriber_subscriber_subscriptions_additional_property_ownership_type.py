from enum import Enum


class SubscriberSubscriberSubscriptionsAdditionalPropertyOwnershipType(str, Enum):
    FAMILY_SHARED = "FAMILY_SHARED"
    PURCHASED = "PURCHASED"

    def __str__(self) -> str:
        return str(self.value)
