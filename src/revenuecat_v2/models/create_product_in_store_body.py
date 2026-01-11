from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_app_store_connect_in_app_purchase_input import CreateAppStoreConnectInAppPurchaseInput
    from ..models.create_app_store_connect_subscription_input import CreateAppStoreConnectSubscriptionInput


T = TypeVar("T", bound="CreateProductInStoreBody")


@_attrs_define
class CreateProductInStoreBody:
    """
    Attributes:
        store_information (CreateAppStoreConnectInAppPurchaseInput | CreateAppStoreConnectSubscriptionInput | Unset):
            Store-specific information for creating the product in the store
    """

    store_information: CreateAppStoreConnectInAppPurchaseInput | CreateAppStoreConnectSubscriptionInput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_app_store_connect_subscription_input import CreateAppStoreConnectSubscriptionInput

        store_information: dict[str, Any] | Unset
        if isinstance(self.store_information, Unset):
            store_information = UNSET
        elif isinstance(self.store_information, CreateAppStoreConnectSubscriptionInput):
            store_information = self.store_information.to_dict()
        else:
            store_information = self.store_information.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if store_information is not UNSET:
            field_dict["store_information"] = store_information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_app_store_connect_in_app_purchase_input import CreateAppStoreConnectInAppPurchaseInput
        from ..models.create_app_store_connect_subscription_input import CreateAppStoreConnectSubscriptionInput

        d = dict(src_dict)

        def _parse_store_information(
            data: object,
        ) -> CreateAppStoreConnectInAppPurchaseInput | CreateAppStoreConnectSubscriptionInput | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                store_information_type_0 = CreateAppStoreConnectSubscriptionInput.from_dict(data)

                return store_information_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            store_information_type_1 = CreateAppStoreConnectInAppPurchaseInput.from_dict(data)

            return store_information_type_1

        store_information = _parse_store_information(d.pop("store_information", UNSET))

        create_product_in_store_body = cls(
            store_information=store_information,
        )

        return create_product_in_store_body
