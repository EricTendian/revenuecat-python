from enum import Enum


class StoreKitConfigFileObject(str, Enum):
    STORE_KIT_CONFIG_FILE = "store_kit_config_file"

    def __str__(self) -> str:
        return str(self.value)
