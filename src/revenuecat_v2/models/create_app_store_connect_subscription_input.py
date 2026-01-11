from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_app_store_connect_subscription_input_duration import CreateAppStoreConnectSubscriptionInputDuration
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAppStoreConnectSubscriptionInput")


@_attrs_define
class CreateAppStoreConnectSubscriptionInput:
    """
    Attributes:
        duration (CreateAppStoreConnectSubscriptionInputDuration): The subscription duration period
        subscription_group_name (str): The name of the subscription group
        subscription_group_id (None | str | Unset): The ID of the subscription group (optional)
    """

    duration: CreateAppStoreConnectSubscriptionInputDuration
    subscription_group_name: str
    subscription_group_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration.value

        subscription_group_name = self.subscription_group_name

        subscription_group_id: None | str | Unset
        if isinstance(self.subscription_group_id, Unset):
            subscription_group_id = UNSET
        else:
            subscription_group_id = self.subscription_group_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "duration": duration,
                "subscription_group_name": subscription_group_name,
            }
        )
        if subscription_group_id is not UNSET:
            field_dict["subscription_group_id"] = subscription_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration = CreateAppStoreConnectSubscriptionInputDuration(d.pop("duration"))

        subscription_group_name = d.pop("subscription_group_name")

        def _parse_subscription_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_group_id = _parse_subscription_group_id(d.pop("subscription_group_id", UNSET))

        create_app_store_connect_subscription_input = cls(
            duration=duration,
            subscription_group_name=subscription_group_name,
            subscription_group_id=subscription_group_id,
        )

        return create_app_store_connect_subscription_input
