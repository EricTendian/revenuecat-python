from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.paywall_object import PaywallObject

T = TypeVar("T", bound="Paywall")


@_attrs_define
class Paywall:
    """
    Attributes:
        object_ (PaywallObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the paywall Example: pw123456789abcdef.
        name (None | str): The name of the paywall Example: My Awesome Paywall.
        offering_id (str): The ID of the offering the paywall is for. Example: ofrng123456789a.
        created_at (int): The date the paywall was created at in ms since epoch Example: 1658399423658.
        published_at (int | None): The date the paywall was published at in ms since epoch Example: 1658399423958.
    """

    object_: PaywallObject
    id: str
    name: None | str
    offering_id: str
    created_at: int
    published_at: int | None

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        name: None | str
        name = self.name

        offering_id = self.offering_id

        created_at = self.created_at

        published_at: int | None
        published_at = self.published_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "offering_id": offering_id,
                "created_at": created_at,
                "published_at": published_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = PaywallObject(d.pop("object"))

        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        offering_id = d.pop("offering_id")

        created_at = d.pop("created_at")

        def _parse_published_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        published_at = _parse_published_at(d.pop("published_at"))

        paywall = cls(
            object_=object_,
            id=id,
            name=name,
            offering_id=offering_id,
            created_at=created_at,
            published_at=published_at,
        )

        return paywall
