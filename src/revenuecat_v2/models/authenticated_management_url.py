from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.authenticated_management_url_object import AuthenticatedManagementUrlObject

T = TypeVar("T", bound="AuthenticatedManagementUrl")


@_attrs_define
class AuthenticatedManagementUrl:
    """
    Attributes:
        object_ (AuthenticatedManagementUrlObject): String representing the object's type. Objects of the same type
            share the same value.
        management_url (str): A secure, single-use URL that provides temporary access to the customer portal for a
            specific customer. This URL can only be used once and expires after use. Example:
            https://billing.revenuecat.com/app1a2b3c4/sub1ab2c3d4e5?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
    """

    object_: AuthenticatedManagementUrlObject
    management_url: str

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        management_url = self.management_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "management_url": management_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = AuthenticatedManagementUrlObject(d.pop("object"))

        management_url = d.pop("management_url")

        authenticated_management_url = cls(
            object_=object_,
            management_url=management_url,
        )

        return authenticated_management_url
