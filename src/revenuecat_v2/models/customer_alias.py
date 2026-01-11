from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.customer_alias_object import CustomerAliasObject

T = TypeVar("T", bound="CustomerAlias")


@_attrs_define
class CustomerAlias:
    """
    Attributes:
        object_ (CustomerAliasObject): String representing the object's type. Objects of the same type share the same
            value.
        id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        created_at (int): The time when the alias was created Example: 1658399423658.
    """

    object_: CustomerAliasObject
    id: str
    created_at: int

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = CustomerAliasObject(d.pop("object"))

        id = d.pop("id")

        created_at = d.pop("created_at")

        customer_alias = cls(
            object_=object_,
            id=id,
            created_at=created_at,
        )

        return customer_alias
