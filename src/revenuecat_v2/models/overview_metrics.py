from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.overview_metrics_object import OverviewMetricsObject

if TYPE_CHECKING:
    from ..models.overview_metric import OverviewMetric


T = TypeVar("T", bound="OverviewMetrics")


@_attrs_define
class OverviewMetrics:
    """
    Attributes:
        object_ (OverviewMetricsObject): String representing the object's type. Objects of the same type share the same
            value.
        metrics (list[OverviewMetric]): Details about each overview metric.
    """

    object_: OverviewMetricsObject
    metrics: list[OverviewMetric]

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "metrics": metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.overview_metric import OverviewMetric

        d = dict(src_dict)
        object_ = OverviewMetricsObject(d.pop("object"))

        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = OverviewMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        overview_metrics = cls(
            object_=object_,
            metrics=metrics,
        )

        return overview_metrics
