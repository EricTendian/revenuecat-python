from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaddleAppCreatePaddleType0")


@_attrs_define
class PaddleAppCreatePaddleType0:
    """Paddle Billing details. Should only be used when type is paddle.

    Attributes:
        paddle_api_key (None | str | Unset): Paddle Server-side API key provided on the Paddle dashboard.
        paddle_is_sandbox (bool | None | Unset): [Deprecated] Whether the app is tied to the sandbox environment.
            This field is deprecated and will be removed in the future.
            The environment is determined by the `paddle_api_key` format.
             Example: True.
    """

    paddle_api_key: None | str | Unset = UNSET
    paddle_is_sandbox: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paddle_api_key: None | str | Unset
        if isinstance(self.paddle_api_key, Unset):
            paddle_api_key = UNSET
        else:
            paddle_api_key = self.paddle_api_key

        paddle_is_sandbox: bool | None | Unset
        if isinstance(self.paddle_is_sandbox, Unset):
            paddle_is_sandbox = UNSET
        else:
            paddle_is_sandbox = self.paddle_is_sandbox

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paddle_api_key is not UNSET:
            field_dict["paddle_api_key"] = paddle_api_key
        if paddle_is_sandbox is not UNSET:
            field_dict["paddle_is_sandbox"] = paddle_is_sandbox

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_paddle_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paddle_api_key = _parse_paddle_api_key(d.pop("paddle_api_key", UNSET))

        def _parse_paddle_is_sandbox(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        paddle_is_sandbox = _parse_paddle_is_sandbox(d.pop("paddle_is_sandbox", UNSET))

        paddle_app_create_paddle_type_0 = cls(
            paddle_api_key=paddle_api_key,
            paddle_is_sandbox=paddle_is_sandbox,
        )

        paddle_app_create_paddle_type_0.additional_properties = d
        return paddle_app_create_paddle_type_0

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
