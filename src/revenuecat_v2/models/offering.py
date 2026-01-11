from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.offering_object import OfferingObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_metadata_type_0 import OfferingMetadataType0
    from ..models.offering_package_list import OfferingPackageList


T = TypeVar("T", bound="Offering")


@_attrs_define
class Offering:
    """
    Attributes:
        object_ (OfferingObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the offering Example: ofrnge1a2b3c4d5.
        lookup_key (str): A custom identifier of the entitlement Example: default.
        display_name (str): The display name of the offering Example: The standard set of packages.
        is_current (bool): Indicates if the offering is the current offering Example: True.
        created_at (int): The date the offering was created at in ms since epoch Example: 1658399423658.
        project_id (str): ID of the project to which the offering belongs Example: proj1ab2c3d4.
        metadata (None | OfferingMetadataType0 | Unset): Custom metadata of the offering Example: {'color': 'blue',
            'call_to_action': 'Subscribe Now!'}.
        packages (None | OfferingPackageList | Unset):
    """

    object_: OfferingObject
    id: str
    lookup_key: str
    display_name: str
    is_current: bool
    created_at: int
    project_id: str
    metadata: None | OfferingMetadataType0 | Unset = UNSET
    packages: None | OfferingPackageList | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.offering_metadata_type_0 import OfferingMetadataType0
        from ..models.offering_package_list import OfferingPackageList

        object_ = self.object_.value

        id = self.id

        lookup_key = self.lookup_key

        display_name = self.display_name

        is_current = self.is_current

        created_at = self.created_at

        project_id = self.project_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, OfferingMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        packages: dict[str, Any] | None | Unset
        if isinstance(self.packages, Unset):
            packages = UNSET
        elif isinstance(self.packages, OfferingPackageList):
            packages = self.packages.to_dict()
        else:
            packages = self.packages

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "lookup_key": lookup_key,
                "display_name": display_name,
                "is_current": is_current,
                "created_at": created_at,
                "project_id": project_id,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if packages is not UNSET:
            field_dict["packages"] = packages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_metadata_type_0 import OfferingMetadataType0
        from ..models.offering_package_list import OfferingPackageList

        d = dict(src_dict)
        object_ = OfferingObject(d.pop("object"))

        id = d.pop("id")

        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

        is_current = d.pop("is_current")

        created_at = d.pop("created_at")

        project_id = d.pop("project_id")

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

        def _parse_packages(data: object) -> None | OfferingPackageList | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                packages_type_0 = OfferingPackageList.from_dict(data)

                return packages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfferingPackageList | Unset, data)

        packages = _parse_packages(d.pop("packages", UNSET))

        offering = cls(
            object_=object_,
            id=id,
            lookup_key=lookup_key,
            display_name=display_name,
            is_current=is_current,
            created_at=created_at,
            project_id=project_id,
            metadata=metadata,
            packages=packages,
        )

        return offering
