from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.webhook_integration_list_object import WebhookIntegrationListObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_integration import WebhookIntegration


T = TypeVar("T", bound="WebhookIntegrationList")


@_attrs_define
class WebhookIntegrationList:
    """
    Attributes:
        object_ (WebhookIntegrationListObject): String representing the object's type. Objects of the same type share
            the
            same value.
        items (list[WebhookIntegration]): Webhook integrations configured for the project.
        url (str): The URL where this list can be accessed. Example: /v2/projects/proj1ab2c3d4/integrations/webhooks.
        next_page (None | str | Unset): URL to access the next page of webhook integrations. If not present / null,
            there is no next page Example: /v2/projects/proj1ab2c3d4/integrations/webhooks?starting_after=whintgr1a2b3c4d.
    """

    object_: WebhookIntegrationListObject
    items: list[WebhookIntegration]
    url: str
    next_page: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        url = self.url

        next_page: None | str | Unset
        if isinstance(self.next_page, Unset):
            next_page = UNSET
        else:
            next_page = self.next_page

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "items": items,
                "url": url,
            }
        )
        if next_page is not UNSET:
            field_dict["next_page"] = next_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_integration import WebhookIntegration

        d = dict(src_dict)
        object_ = WebhookIntegrationListObject(d.pop("object"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = WebhookIntegration.from_dict(items_item_data)

            items.append(items_item)

        url = d.pop("url")

        def _parse_next_page(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page = _parse_next_page(d.pop("next_page", UNSET))

        webhook_integration_list = cls(
            object_=object_,
            items=items,
            url=url,
            next_page=next_page,
        )

        return webhook_integration_list
