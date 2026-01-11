from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_metadata_type_0 import OfferingMetadataType0


T = TypeVar("T", bound="UpdateOfferingBody")


@_attrs_define
class UpdateOfferingBody:
    """
    Attributes:
        display_name (str | Unset): The display name of the offering Example: premium access to features.
        is_current (bool | Unset): Indicates if the offering is the current offering Example: True.
        metadata (None | OfferingMetadataType0 | Unset): Custom metadata of the offering Example: {'color': 'blue',
            'call_to_action': 'Subscribe Now!'}.
    """

    display_name: str | Unset = UNSET
    is_current: bool | Unset = UNSET
    metadata: None | OfferingMetadataType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.offering_metadata_type_0 import OfferingMetadataType0

        display_name = self.display_name

        is_current = self.is_current

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, OfferingMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if is_current is not UNSET:
            field_dict["is_current"] = is_current
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_metadata_type_0 import OfferingMetadataType0

        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        is_current = d.pop("is_current", UNSET)

        def _parse_metadata(data: object) -> None | OfferingMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_offering_metadata_type_0 = OfferingMetadataType0.from_dict(data)

                return componentsschemas_offering_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfferingMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        update_offering_body = cls(
            display_name=display_name,
            is_current=is_current,
            metadata=metadata,
        )

        return update_offering_body
