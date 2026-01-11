from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.webhook_integration_environment_type_1 import WebhookIntegrationEnvironmentType1
from ..models.webhook_integration_environment_type_2_type_1 import WebhookIntegrationEnvironmentType2Type1
from ..models.webhook_integration_environment_type_3_type_1 import WebhookIntegrationEnvironmentType3Type1
from ..models.webhook_integration_object import WebhookIntegrationObject
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookIntegration")


@_attrs_define
class WebhookIntegration:
    """
    Attributes:
        object_ (WebhookIntegrationObject): String representing the object's type. Objects of the same type share the
            same value.
        id (str): The ID of the webhook integration Example: wh_1234567890abcdef.
        project_id (str): The ID of the project the webhook integration belongs to Example: proj_1234567890abcdef.
        name (str): The display name of the webhook integration Example: Customer updates webhook.
        url (str): The URL RevenueCat will send webhook notifications to Example: https://hooks.example.com/revenuecat.
        environment (None | WebhookIntegrationEnvironmentType1 | WebhookIntegrationEnvironmentType2Type1 |
            WebhookIntegrationEnvironmentType3Type1): The environment the webhook integration is configured for. Only events
            for the selected environment will be sent.
        app_id (None | str): The ID of the app the webhook integration is scoped to. If not provided, the webhook
            integration will be scoped to all apps in the project. Example: app_1234567890abcdef.
        created_at (int): The timestamp in ms since epoch when the webhook integration was created Example:
            1658399423658.
        event_types (list[str] | None | Unset): Event types that will trigger the webhook. Only events for the selected
            event types will be sent.
    """

    object_: WebhookIntegrationObject
    id: str
    project_id: str
    name: str
    url: str
    environment: (
        None
        | WebhookIntegrationEnvironmentType1
        | WebhookIntegrationEnvironmentType2Type1
        | WebhookIntegrationEnvironmentType3Type1
    )
    app_id: None | str
    created_at: int
    event_types: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        project_id = self.project_id

        name = self.name

        url = self.url

        environment: None | str
        if isinstance(self.environment, WebhookIntegrationEnvironmentType1):
            environment = self.environment.value
        elif isinstance(self.environment, WebhookIntegrationEnvironmentType2Type1):
            environment = self.environment.value
        elif isinstance(self.environment, WebhookIntegrationEnvironmentType3Type1):
            environment = self.environment.value
        else:
            environment = self.environment

        app_id: None | str
        app_id = self.app_id

        created_at = self.created_at

        event_types: list[str] | None | Unset
        if isinstance(self.event_types, Unset):
            event_types = UNSET
        elif isinstance(self.event_types, list):
            event_types = self.event_types

        else:
            event_types = self.event_types

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "project_id": project_id,
                "name": name,
                "url": url,
                "environment": environment,
                "app_id": app_id,
                "created_at": created_at,
            }
        )
        if event_types is not UNSET:
            field_dict["event_types"] = event_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = WebhookIntegrationObject(d.pop("object"))

        id = d.pop("id")

        project_id = d.pop("project_id")

        name = d.pop("name")

        url = d.pop("url")

        def _parse_environment(
            data: object,
        ) -> (
            None
            | WebhookIntegrationEnvironmentType1
            | WebhookIntegrationEnvironmentType2Type1
            | WebhookIntegrationEnvironmentType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_type_1 = WebhookIntegrationEnvironmentType1(data)

                return environment_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_type_2_type_1 = WebhookIntegrationEnvironmentType2Type1(data)

                return environment_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_type_3_type_1 = WebhookIntegrationEnvironmentType3Type1(data)

                return environment_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | WebhookIntegrationEnvironmentType1
                | WebhookIntegrationEnvironmentType2Type1
                | WebhookIntegrationEnvironmentType3Type1,
                data,
            )

        environment = _parse_environment(d.pop("environment"))

        def _parse_app_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        app_id = _parse_app_id(d.pop("app_id"))

        created_at = d.pop("created_at")

        def _parse_event_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = cast(list[str], data)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        event_types = _parse_event_types(d.pop("event_types", UNSET))

        webhook_integration = cls(
            object_=object_,
            id=id,
            project_id=project_id,
            name=name,
            url=url,
            environment=environment,
            app_id=app_id,
            created_at=created_at,
            event_types=event_types,
        )

        return webhook_integration
