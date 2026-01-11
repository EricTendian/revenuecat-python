from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paddle_app_create_paddle_type_0 import PaddleAppCreatePaddleType0


T = TypeVar("T", bound="PaddleAppCreate")


@_attrs_define
class PaddleAppCreate:
    """
    Attributes:
        paddle (None | PaddleAppCreatePaddleType0 | Unset): Paddle Billing details. Should only be used when type is
            paddle.
    """

    paddle: None | PaddleAppCreatePaddleType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paddle_app_create_paddle_type_0 import PaddleAppCreatePaddleType0

        paddle: dict[str, Any] | None | Unset
        if isinstance(self.paddle, Unset):
            paddle = UNSET
        elif isinstance(self.paddle, PaddleAppCreatePaddleType0):
            paddle = self.paddle.to_dict()
        else:
            paddle = self.paddle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paddle is not UNSET:
            field_dict["paddle"] = paddle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paddle_app_create_paddle_type_0 import PaddleAppCreatePaddleType0

        d = dict(src_dict)

        def _parse_paddle(data: object) -> None | PaddleAppCreatePaddleType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                paddle_type_0 = PaddleAppCreatePaddleType0.from_dict(data)

                return paddle_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaddleAppCreatePaddleType0 | Unset, data)

        paddle = _parse_paddle(d.pop("paddle", UNSET))

        paddle_app_create = cls(
            paddle=paddle,
        )

        paddle_app_create.additional_properties = d
        return paddle_app_create

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
