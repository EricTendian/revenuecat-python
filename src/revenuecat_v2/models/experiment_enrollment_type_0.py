from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.experiment_enrollment_type_0_object import ExperimentEnrollmentType0Object

T = TypeVar("T", bound="ExperimentEnrollmentType0")


@_attrs_define
class ExperimentEnrollmentType0:
    """
    Attributes:
        object_ (ExperimentEnrollmentType0Object): String representing the object's type. Objects of the same type share
            the same value.
        id (str):
        name (str):
        variant (str): The variant of the Experiment that the Customer was or is assigned to, where 'a' represents the
            Control, and 'b' represents the Treatment. Example: a.
    """

    object_: ExperimentEnrollmentType0Object
    id: str
    name: str
    variant: str

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        name = self.name

        variant = self.variant

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "variant": variant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = ExperimentEnrollmentType0Object(d.pop("object"))

        id = d.pop("id")

        name = d.pop("name")

        variant = d.pop("variant")

        experiment_enrollment_type_0 = cls(
            object_=object_,
            id=id,
            name=name,
            variant=variant,
        )

        return experiment_enrollment_type_0
