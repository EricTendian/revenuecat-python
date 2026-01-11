from enum import Enum


class AttachProductsToPackageResponse400Type(str, Enum):
    INVALID_REQUEST = "invalid_request"
    PARAMETER_ERROR = "parameter_error"

    def __str__(self) -> str:
        return str(self.value)
