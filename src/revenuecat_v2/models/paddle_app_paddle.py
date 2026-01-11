from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaddleAppPaddle")


@_attrs_define
class PaddleAppPaddle:
    """Paddle Billing type details

    Attributes:
        paddle_is_sandbox (bool | Unset): Whether the app is tied to the sandbox environment. Example: True.
        paddle_api_key (None | str | Unset): Paddle Server-side API key provided on the Paddle dashboard.
    """

    paddle_is_sandbox: bool | Unset = UNSET
    paddle_api_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paddle_is_sandbox = self.paddle_is_sandbox

        paddle_api_key: None | str | Unset
        if isinstance(self.paddle_api_key, Unset):
            paddle_api_key = UNSET
        else:
            paddle_api_key = self.paddle_api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paddle_is_sandbox is not UNSET:
            field_dict["paddle_is_sandbox"] = paddle_is_sandbox
        if paddle_api_key is not UNSET:
            field_dict["paddle_api_key"] = paddle_api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        paddle_is_sandbox = d.pop("paddle_is_sandbox", UNSET)

        def _parse_paddle_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paddle_api_key = _parse_paddle_api_key(d.pop("paddle_api_key", UNSET))

        paddle_app_paddle = cls(
            paddle_is_sandbox=paddle_is_sandbox,
            paddle_api_key=paddle_api_key,
        )

        paddle_app_paddle.additional_properties = d
        return paddle_app_paddle

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
