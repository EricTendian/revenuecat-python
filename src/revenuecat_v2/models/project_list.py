from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.project_list_object import ProjectListObject

if TYPE_CHECKING:
    from ..models.project import Project


T = TypeVar("T", bound="ProjectList")


@_attrs_define
class ProjectList:
    """
    Attributes:
        object_ (ProjectListObject): String representing the object's type. Objects of the same type share the same
            value. Always has the value `list`.
        items (list[Project]): Details about each object.
        next_page (None | str): URL to access the next page of the projects. If not present / null, there is no next
            page Example: /v2/projects?starting_after=projab21dac.
        url (str): The URL where this list can be accessed. Example: /v2/projects.
    """

    object_: ProjectListObject
    items: list[Project]
    next_page: None | str
    url: str

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_page: None | str
        next_page = self.next_page

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "items": items,
                "next_page": next_page,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project import Project

        d = dict(src_dict)
        object_ = ProjectListObject(d.pop("object"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Project.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_page(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_page = _parse_next_page(d.pop("next_page"))

        url = d.pop("url")

        project_list = cls(
            object_=object_,
            items=items,
            next_page=next_page,
            url=url,
        )

        return project_list
