from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.project_object import ProjectObject
from ..types import UNSET, Unset

T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """
    Attributes:
        object_ (ProjectObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the project Example: proj1ab2c3d4.
        name (str): The name of the project Example: MagicWeather.
        created_at (int): The date when the project was created in ms since epoch Example: 1658399423658.
        icon_url (None | str | Unset): The URL of the project's icon (small size) Example:
            https://www.appatar.io/abc123/small.
        icon_url_large (None | str | Unset): The URL of the project's icon (large size) Example:
            https://www.appatar.io/abc123/large.
    """

    object_: ProjectObject
    id: str
    name: str
    created_at: int
    icon_url: None | str | Unset = UNSET
    icon_url_large: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        name = self.name

        created_at = self.created_at

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        icon_url_large: None | str | Unset
        if isinstance(self.icon_url_large, Unset):
            icon_url_large = UNSET
        else:
            icon_url_large = self.icon_url_large

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "created_at": created_at,
            }
        )
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if icon_url_large is not UNSET:
            field_dict["icon_url_large"] = icon_url_large

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = ProjectObject(d.pop("object"))

        id = d.pop("id")

        name = d.pop("name")

        created_at = d.pop("created_at")

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("icon_url", UNSET))

        def _parse_icon_url_large(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url_large = _parse_icon_url_large(d.pop("icon_url_large", UNSET))

        project = cls(
            object_=object_,
            id=id,
            name=name,
            created_at=created_at,
            icon_url=icon_url,
            icon_url_large=icon_url_large,
        )

        return project
