from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppStoreAppCreateAppStore")


@_attrs_define
class AppStoreAppCreateAppStore:
    """App Store type details. Should only be used when type is app_store.

    Attributes:
        bundle_id (str): The bundle ID of the app
        shared_secret (str | Unset): The shared secret of the app
        subscription_private_key (str | Unset): PKCS /#8 In App Key downloaded from App Store Connect in PEM format.
            Copy the contents
            of the file in this field. See instructions on how to get it in:
            https://www.revenuecat.com/docs/in-app-purchase-key-configuration
        subscription_key_id (str | Unset): In App Key id. The ID of the downloaded in app key. You can get it from App
            Store Connect
        subscription_key_issuer (str | Unset): The key Issuer id. See instructions on how to obtain this in:
            https://www.revenuecat.com/docs/in-app-purchase-key-configuration#3-providing-the-issuer-id-to-revenuecat
        app_store_connect_api_key (str | Unset): App Store Connect API Key downloaded from App Store Connect in PEM
            format. Copy the contents
            of the file in this field. This is optional and used for advanced features like product imports.
        app_store_connect_api_key_id (str | Unset): App Store Connect API Key ID. The ID of the downloaded API key. You
            can get it from App Store Connect.
        app_store_connect_api_key_issuer (str | Unset): App Store Connect API Key Issuer ID.
        app_store_connect_vendor_number (str | Unset): Your vendor number from App Store Connect. Required for some
            features like financial reports.
    """

    bundle_id: str
    shared_secret: str | Unset = UNSET
    subscription_private_key: str | Unset = UNSET
    subscription_key_id: str | Unset = UNSET
    subscription_key_issuer: str | Unset = UNSET
    app_store_connect_api_key: str | Unset = UNSET
    app_store_connect_api_key_id: str | Unset = UNSET
    app_store_connect_api_key_issuer: str | Unset = UNSET
    app_store_connect_vendor_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bundle_id = self.bundle_id

        shared_secret = self.shared_secret

        subscription_private_key = self.subscription_private_key

        subscription_key_id = self.subscription_key_id

        subscription_key_issuer = self.subscription_key_issuer

        app_store_connect_api_key = self.app_store_connect_api_key

        app_store_connect_api_key_id = self.app_store_connect_api_key_id

        app_store_connect_api_key_issuer = self.app_store_connect_api_key_issuer

        app_store_connect_vendor_number = self.app_store_connect_vendor_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bundle_id": bundle_id,
            }
        )
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret
        if subscription_private_key is not UNSET:
            field_dict["subscription_private_key"] = subscription_private_key
        if subscription_key_id is not UNSET:
            field_dict["subscription_key_id"] = subscription_key_id
        if subscription_key_issuer is not UNSET:
            field_dict["subscription_key_issuer"] = subscription_key_issuer
        if app_store_connect_api_key is not UNSET:
            field_dict["app_store_connect_api_key"] = app_store_connect_api_key
        if app_store_connect_api_key_id is not UNSET:
            field_dict["app_store_connect_api_key_id"] = app_store_connect_api_key_id
        if app_store_connect_api_key_issuer is not UNSET:
            field_dict["app_store_connect_api_key_issuer"] = app_store_connect_api_key_issuer
        if app_store_connect_vendor_number is not UNSET:
            field_dict["app_store_connect_vendor_number"] = app_store_connect_vendor_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bundle_id = d.pop("bundle_id")

        shared_secret = d.pop("shared_secret", UNSET)

        subscription_private_key = d.pop("subscription_private_key", UNSET)

        subscription_key_id = d.pop("subscription_key_id", UNSET)

        subscription_key_issuer = d.pop("subscription_key_issuer", UNSET)

        app_store_connect_api_key = d.pop("app_store_connect_api_key", UNSET)

        app_store_connect_api_key_id = d.pop("app_store_connect_api_key_id", UNSET)

        app_store_connect_api_key_issuer = d.pop("app_store_connect_api_key_issuer", UNSET)

        app_store_connect_vendor_number = d.pop("app_store_connect_vendor_number", UNSET)

        app_store_app_create_app_store = cls(
            bundle_id=bundle_id,
            shared_secret=shared_secret,
            subscription_private_key=subscription_private_key,
            subscription_key_id=subscription_key_id,
            subscription_key_issuer=subscription_key_issuer,
            app_store_connect_api_key=app_store_connect_api_key,
            app_store_connect_api_key_id=app_store_connect_api_key_id,
            app_store_connect_api_key_issuer=app_store_connect_api_key_issuer,
            app_store_connect_vendor_number=app_store_connect_vendor_number,
        )

        app_store_app_create_app_store.additional_properties = d
        return app_store_app_create_app_store

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
