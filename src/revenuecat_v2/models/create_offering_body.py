from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_metadata_type_0 import OfferingMetadataType0


T = TypeVar("T", bound="CreateOfferingBody")


@_attrs_define
class CreateOfferingBody:
    """
    Attributes:
        lookup_key (str): The custom identifier of the offering Example: default.
        display_name (str): The display_name of the offering Example: The standard set of packages.
        metadata (None | OfferingMetadataType0 | Unset): Custom metadata of the offering Example: {'color': 'blue',
            'call_to_action': 'Subscribe Now!'}.
    """

    lookup_key: str
    display_name: str
    metadata: None | OfferingMetadataType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.offering_metadata_type_0 import OfferingMetadataType0

        lookup_key = self.lookup_key

        display_name = self.display_name

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, OfferingMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "lookup_key": lookup_key,
                "display_name": display_name,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_metadata_type_0 import OfferingMetadataType0

        d = dict(src_dict)
        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

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

        create_offering_body = cls(
            lookup_key=lookup_key,
            display_name=display_name,
            metadata=metadata,
        )

        return create_offering_body
