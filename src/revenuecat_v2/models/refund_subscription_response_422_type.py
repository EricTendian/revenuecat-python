from enum import Enum


class RefundSubscriptionResponse422Type(str, Enum):
    PARAMETER_ERROR = "parameter_error"
    STORE_ERROR = "store_error"
    UNPROCESSABLE_ENTITY_ERROR = "unprocessable_entity_error"

    def __str__(self) -> str:
        return str(self.value)
