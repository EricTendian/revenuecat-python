from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.customer_object import CustomerObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_active_entitlements import CustomerActiveEntitlements
    from ..models.customer_attributes import CustomerAttributes
    from ..models.experiment_enrollment_type_0 import ExperimentEnrollmentType0


T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    """
    Attributes:
        object_ (CustomerObject): String representing the object's type. Objects of the same type share the same value.
        id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        project_id (str): ID of the project to which the customer belongs Example: proj1ab2c3d4.
        first_seen_at (int): The first time the customer was seen Example: 1658399423658.
        last_seen_at (int | None): The last time the customer was seen Example: 1658399423658.
        last_seen_app_version (None | str): The last app version the customer was seen on Example: 1.0.0.
        last_seen_country (None | str): The last country the customer was seen in Example: US.
        last_seen_platform (None | str): The last platform the customer was seen on Example: android.
        last_seen_platform_version (None | str): The last platform version the customer was seen on Example: 35.
        active_entitlements (CustomerActiveEntitlements | Unset):
        experiment (ExperimentEnrollmentType0 | None | Unset):
        attributes (CustomerAttributes | Unset):
    """

    object_: CustomerObject
    id: str
    project_id: str
    first_seen_at: int
    last_seen_at: int | None
    last_seen_app_version: None | str
    last_seen_country: None | str
    last_seen_platform: None | str
    last_seen_platform_version: None | str
    active_entitlements: CustomerActiveEntitlements | Unset = UNSET
    experiment: ExperimentEnrollmentType0 | None | Unset = UNSET
    attributes: CustomerAttributes | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_enrollment_type_0 import ExperimentEnrollmentType0

        object_ = self.object_.value

        id = self.id

        project_id = self.project_id

        first_seen_at = self.first_seen_at

        last_seen_at: int | None
        last_seen_at = self.last_seen_at

        last_seen_app_version: None | str
        last_seen_app_version = self.last_seen_app_version

        last_seen_country: None | str
        last_seen_country = self.last_seen_country

        last_seen_platform: None | str
        last_seen_platform = self.last_seen_platform

        last_seen_platform_version: None | str
        last_seen_platform_version = self.last_seen_platform_version

        active_entitlements: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_entitlements, Unset):
            active_entitlements = self.active_entitlements.to_dict()

        experiment: dict[str, Any] | None | Unset
        if isinstance(self.experiment, Unset):
            experiment = UNSET
        elif isinstance(self.experiment, ExperimentEnrollmentType0):
            experiment = self.experiment.to_dict()
        else:
            experiment = self.experiment

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "project_id": project_id,
                "first_seen_at": first_seen_at,
                "last_seen_at": last_seen_at,
                "last_seen_app_version": last_seen_app_version,
                "last_seen_country": last_seen_country,
                "last_seen_platform": last_seen_platform,
                "last_seen_platform_version": last_seen_platform_version,
            }
        )
        if active_entitlements is not UNSET:
            field_dict["active_entitlements"] = active_entitlements
        if experiment is not UNSET:
            field_dict["experiment"] = experiment
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer_active_entitlements import CustomerActiveEntitlements
        from ..models.customer_attributes import CustomerAttributes
        from ..models.experiment_enrollment_type_0 import ExperimentEnrollmentType0

        d = dict(src_dict)
        object_ = CustomerObject(d.pop("object"))

        id = d.pop("id")

        project_id = d.pop("project_id")

        first_seen_at = d.pop("first_seen_at")

        def _parse_last_seen_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_seen_at = _parse_last_seen_at(d.pop("last_seen_at"))

        def _parse_last_seen_app_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_seen_app_version = _parse_last_seen_app_version(d.pop("last_seen_app_version"))

        def _parse_last_seen_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_seen_country = _parse_last_seen_country(d.pop("last_seen_country"))

        def _parse_last_seen_platform(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_seen_platform = _parse_last_seen_platform(d.pop("last_seen_platform"))

        def _parse_last_seen_platform_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_seen_platform_version = _parse_last_seen_platform_version(d.pop("last_seen_platform_version"))

        _active_entitlements = d.pop("active_entitlements", UNSET)
        active_entitlements: CustomerActiveEntitlements | Unset
        if isinstance(_active_entitlements, Unset):
            active_entitlements = UNSET
        else:
            active_entitlements = CustomerActiveEntitlements.from_dict(_active_entitlements)

        def _parse_experiment(data: object) -> ExperimentEnrollmentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_experiment_enrollment_type_0 = ExperimentEnrollmentType0.from_dict(data)

                return componentsschemas_experiment_enrollment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExperimentEnrollmentType0 | None | Unset, data)

        experiment = _parse_experiment(d.pop("experiment", UNSET))

        _attributes = d.pop("attributes", UNSET)
        attributes: CustomerAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = CustomerAttributes.from_dict(_attributes)

        customer = cls(
            object_=object_,
            id=id,
            project_id=project_id,
            first_seen_at=first_seen_at,
            last_seen_at=last_seen_at,
            last_seen_app_version=last_seen_app_version,
            last_seen_country=last_seen_country,
            last_seen_platform=last_seen_platform,
            last_seen_platform_version=last_seen_platform_version,
            active_entitlements=active_entitlements,
            experiment=experiment,
            attributes=attributes,
        )

        return customer
