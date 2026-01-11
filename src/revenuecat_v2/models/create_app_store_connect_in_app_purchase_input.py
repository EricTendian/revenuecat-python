from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateAppStoreConnectInAppPurchaseInput")


@_attrs_define
class CreateAppStoreConnectInAppPurchaseInput:
    """In-app purchase products do not require any additional information"""

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        create_app_store_connect_in_app_purchase_input = cls()

        return create_app_store_connect_in_app_purchase_input
