from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.overview_metric_object import OverviewMetricObject
from ..models.overview_metric_period import OverviewMetricPeriod

T = TypeVar("T", bound="OverviewMetric")


@_attrs_define
class OverviewMetric:
    """
    Attributes:
        object_ (OverviewMetricObject): String representing the object's type. Objects of the same type share the same
            value.
        id (str): Id of the overview metric Example: active_trials.
        name (str): Display name of the overview metric Example: Active Trials.
        description (str): Description of the overview metric
        unit (str): Unit of the overview metric Example: $.
        period (OverviewMetricPeriod): Length of time during which metric data is collected in ISO 8601 format. Zero
            period means metric data was collected now Example: P0D.
        value (float): Value of the overview metric Example: 34765.
        last_updated_at (int | None): Last time the overview metric was updated in ms since epoch Example:
            1658399423658.
        last_updated_at_iso8601 (datetime.datetime | None): Last time the overview metric was updated datetime in ISO
            8601 format Example: 2022-10-13 09:45:00.123000+00:00.
    """

    object_: OverviewMetricObject
    id: str
    name: str
    description: str
    unit: str
    period: OverviewMetricPeriod
    value: float
    last_updated_at: int | None
    last_updated_at_iso8601: datetime.datetime | None

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        name = self.name

        description = self.description

        unit = self.unit

        period = self.period.value

        value = self.value

        last_updated_at: int | None
        last_updated_at = self.last_updated_at

        last_updated_at_iso8601: None | str
        if isinstance(self.last_updated_at_iso8601, datetime.datetime):
            last_updated_at_iso8601 = self.last_updated_at_iso8601.isoformat()
        else:
            last_updated_at_iso8601 = self.last_updated_at_iso8601

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "description": description,
                "unit": unit,
                "period": period,
                "value": value,
                "last_updated_at": last_updated_at,
                "last_updated_at_iso8601": last_updated_at_iso8601,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = OverviewMetricObject(d.pop("object"))

        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        unit = d.pop("unit")

        period = OverviewMetricPeriod(d.pop("period"))

        value = d.pop("value")

        def _parse_last_updated_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_updated_at = _parse_last_updated_at(d.pop("last_updated_at"))

        def _parse_last_updated_at_iso8601(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_at_iso8601_type_0 = isoparse(data)

                return last_updated_at_iso8601_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_updated_at_iso8601 = _parse_last_updated_at_iso8601(d.pop("last_updated_at_iso8601"))

        overview_metric = cls(
            object_=object_,
            id=id,
            name=name,
            description=description,
            unit=unit,
            period=period,
            value=value,
            last_updated_at=last_updated_at,
            last_updated_at_iso8601=last_updated_at_iso8601,
        )

        return overview_metric
