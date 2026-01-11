from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.deleted_object_object import DeletedObjectObject

T = TypeVar("T", bound="DeletedObject")


@_attrs_define
class DeletedObject:
    """
    Attributes:
        object_ (DeletedObjectObject): The type of the deleted object
        id (str): The ID of the deleted object
        deleted_at (int): The date when the object was deleted in ms since epoch Example: 1658399423658.
    """

    object_: DeletedObjectObject
    id: str
    deleted_at: int

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "deleted_at": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = DeletedObjectObject(d.pop("object"))

        id = d.pop("id")

        deleted_at = d.pop("deleted_at")

        deleted_object = cls(
            object_=object_,
            id=id,
            deleted_at=deleted_at,
        )

        return deleted_object
