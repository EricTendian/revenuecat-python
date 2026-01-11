from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferCustomerDataBody")


@_attrs_define
class TransferCustomerDataBody:
    """
    Attributes:
        target_customer_id (str): The ID of the customer to whom the subscriptions and one-time purchases will be
            transferred.
        app_ids (list[str] | None | Unset): Optional. The IDs of the apps to filter the transfer by. When specified,
            only purchases and subscriptions associated with these apps will be transferred.
    """

    target_customer_id: str
    app_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_customer_id = self.target_customer_id

        app_ids: list[str] | None | Unset
        if isinstance(self.app_ids, Unset):
            app_ids = UNSET
        elif isinstance(self.app_ids, list):
            app_ids = self.app_ids

        else:
            app_ids = self.app_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "target_customer_id": target_customer_id,
            }
        )
        if app_ids is not UNSET:
            field_dict["app_ids"] = app_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_customer_id = d.pop("target_customer_id")

        def _parse_app_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                app_ids_type_0 = cast(list[str], data)

                return app_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        app_ids = _parse_app_ids(d.pop("app_ids", UNSET))

        transfer_customer_data_body = cls(
            target_customer_id=target_customer_id,
            app_ids=app_ids,
        )

        return transfer_customer_data_body
