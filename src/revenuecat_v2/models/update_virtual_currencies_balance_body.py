from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_virtual_currencies_balance_body_adjustments import (
        UpdateVirtualCurrenciesBalanceBodyAdjustments,
    )


T = TypeVar("T", bound="UpdateVirtualCurrenciesBalanceBody")


@_attrs_define
class UpdateVirtualCurrenciesBalanceBody:
    """
    Attributes:
        adjustments (UpdateVirtualCurrenciesBalanceBodyAdjustments): The adjustments to the virtual currencies
        reference (None | str | Unset): The reference of the transaction
    """

    adjustments: UpdateVirtualCurrenciesBalanceBodyAdjustments
    reference: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        adjustments = self.adjustments.to_dict()

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "adjustments": adjustments,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_virtual_currencies_balance_body_adjustments import (
            UpdateVirtualCurrenciesBalanceBodyAdjustments,
        )

        d = dict(src_dict)
        adjustments = UpdateVirtualCurrenciesBalanceBodyAdjustments.from_dict(d.pop("adjustments"))

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        update_virtual_currencies_balance_body = cls(
            adjustments=adjustments,
            reference=reference,
        )

        return update_virtual_currencies_balance_body
