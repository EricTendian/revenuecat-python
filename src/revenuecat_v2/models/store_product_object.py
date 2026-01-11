from enum import Enum


class StoreProductObject(str, Enum):
    STORE_PRODUCT = "store_product"

    def __str__(self) -> str:
        return str(self.value)
