from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.store_kit_config_file_object import StoreKitConfigFileObject

if TYPE_CHECKING:
    from ..models.store_kit_config_file_contents import StoreKitConfigFileContents


T = TypeVar("T", bound="StoreKitConfigFile")


@_attrs_define
class StoreKitConfigFile:
    """Contents of a generated StoreKit config file for an app

    Attributes:
        object_ (StoreKitConfigFileObject): String representing the object's type. Objects of the same type share the
            same value.
        contents (StoreKitConfigFileContents): Contents of the StoreKit config file
    """

    object_: StoreKitConfigFileObject
    contents: StoreKitConfigFileContents

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        contents = self.contents.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "contents": contents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.store_kit_config_file_contents import StoreKitConfigFileContents

        d = dict(src_dict)
        object_ = StoreKitConfigFileObject(d.pop("object"))

        contents = StoreKitConfigFileContents.from_dict(d.pop("contents"))

        store_kit_config_file = cls(
            object_=object_,
            contents=contents,
        )

        return store_kit_config_file
