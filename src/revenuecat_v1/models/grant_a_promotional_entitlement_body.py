from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grant_a_promotional_entitlement_body_duration import GrantAPromotionalEntitlementBodyDuration
from ..types import UNSET, Unset

T = TypeVar("T", bound="GrantAPromotionalEntitlementBody")


@_attrs_define
class GrantAPromotionalEntitlementBody:
    """
    Attributes:
        end_time_ms (int | Unset): A Unix epoch in milliseconds for when the entitlement should expire. The entitlement
            will always be granted immediately. If not provided then `duration` must be provided. Example: 1709196532093.
        duration (GrantAPromotionalEntitlementBodyDuration | Unset): How long of a duration to grant the entitlement
            for.  If not provided then `end_time_ms` must be provided.
        start_time_ms (int | Unset): A Unix epoch in milliseconds used to determine the expiration date, by adding
            `duration` to `start_time_ms`. Regardless of what `start_time_ms` is set to, the entitlement will always be
            granted immediately. If `start_time_ms` is not provided, the `duration` will be added to the current time to
            determine the expiration date. Example: 1709195668093.
    """

    end_time_ms: int | Unset = UNSET
    duration: GrantAPromotionalEntitlementBodyDuration | Unset = UNSET
    start_time_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time_ms = self.end_time_ms

        duration: str | Unset = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.value

        start_time_ms = self.start_time_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time_ms is not UNSET:
            field_dict["end_time_ms"] = end_time_ms
        if duration is not UNSET:
            field_dict["duration"] = duration
        if start_time_ms is not UNSET:
            field_dict["start_time_ms"] = start_time_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_time_ms = d.pop("end_time_ms", UNSET)

        _duration = d.pop("duration", UNSET)
        duration: GrantAPromotionalEntitlementBodyDuration | Unset
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = GrantAPromotionalEntitlementBodyDuration(_duration)

        start_time_ms = d.pop("start_time_ms", UNSET)

        grant_a_promotional_entitlement_body = cls(
            end_time_ms=end_time_ms,
            duration=duration,
            start_time_ms=start_time_ms,
        )

        grant_a_promotional_entitlement_body.additional_properties = d
        return grant_a_promotional_entitlement_body

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
