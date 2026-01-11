from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAppBodyAmazon")


@_attrs_define
class UpdateAppBodyAmazon:
    """Amazon type details. Should only be used when type is amazon.

    Attributes:
        package_name (str | Unset): The package name of the app
        shared_secret (None | str | Unset): Your Amazon Developer Identity Shared Key
    """

    package_name: str | Unset = UNSET
    shared_secret: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_name = self.package_name

        shared_secret: None | str | Unset
        if isinstance(self.shared_secret, Unset):
            shared_secret = UNSET
        else:
            shared_secret = self.shared_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_name is not UNSET:
            field_dict["package_name"] = package_name
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_name = d.pop("package_name", UNSET)

        def _parse_shared_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shared_secret = _parse_shared_secret(d.pop("shared_secret", UNSET))

        update_app_body_amazon = cls(
            package_name=package_name,
            shared_secret=shared_secret,
        )

        update_app_body_amazon.additional_properties = d
        return update_app_body_amazon

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
