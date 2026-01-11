from enum import Enum


class SubscriberSubscriberSubscriptionsAdditionalPropertyPeriodType(str, Enum):
    INTRO = "intro"
    NORMAL = "normal"
    TRIAL = "trial"

    def __str__(self) -> str:
        return str(self.value)
