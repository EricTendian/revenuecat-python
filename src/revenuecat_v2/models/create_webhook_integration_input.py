from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_webhook_integration_input_environment_type_1 import CreateWebhookIntegrationInputEnvironmentType1
from ..models.create_webhook_integration_input_environment_type_2_type_1 import (
    CreateWebhookIntegrationInputEnvironmentType2Type1,
)
from ..models.create_webhook_integration_input_environment_type_3_type_1 import (
    CreateWebhookIntegrationInputEnvironmentType3Type1,
)
from ..models.webhook_event_type import WebhookEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookIntegrationInput")


@_attrs_define
class CreateWebhookIntegrationInput:
    """
    Attributes:
        name (str): The display name of the webhook integration Example: Customer updates webhook.
        url (str): The URL RevenueCat will send webhook notifications to Example: https://hooks.example.com/revenuecat.
        authorization_header (None | str | Unset): Optional authorization header that will be sent with webhook
            notifications Example: Bearer 123456.
        environment (CreateWebhookIntegrationInputEnvironmentType1 | CreateWebhookIntegrationInputEnvironmentType2Type1
            | CreateWebhookIntegrationInputEnvironmentType3Type1 | None | Unset): The environment the webhook integration is
            configured for
        event_types (list[WebhookEventType] | None | Unset): Event types that will trigger the webhook
        app_id (None | str | Unset): The ID of the app the webhook integration is scoped to Example:
            app_1234567890abcdef.
    """

    name: str
    url: str
    authorization_header: None | str | Unset = UNSET
    environment: (
        CreateWebhookIntegrationInputEnvironmentType1
        | CreateWebhookIntegrationInputEnvironmentType2Type1
        | CreateWebhookIntegrationInputEnvironmentType3Type1
        | None
        | Unset
    ) = UNSET
    event_types: list[WebhookEventType] | None | Unset = UNSET
    app_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        authorization_header: None | str | Unset
        if isinstance(self.authorization_header, Unset):
            authorization_header = UNSET
        else:
            authorization_header = self.authorization_header

        environment: None | str | Unset
        if isinstance(self.environment, Unset):
            environment = UNSET
        elif isinstance(self.environment, CreateWebhookIntegrationInputEnvironmentType1):
            environment = self.environment.value
        elif isinstance(self.environment, CreateWebhookIntegrationInputEnvironmentType2Type1):
            environment = self.environment.value
        elif isinstance(self.environment, CreateWebhookIntegrationInputEnvironmentType3Type1):
            environment = self.environment.value
        else:
            environment = self.environment

        event_types: list[str] | None | Unset
        if isinstance(self.event_types, Unset):
            event_types = UNSET
        elif isinstance(self.event_types, list):
            event_types = []
            for event_types_type_0_item_data in self.event_types:
                event_types_type_0_item = event_types_type_0_item_data.value
                event_types.append(event_types_type_0_item)

        else:
            event_types = self.event_types

        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        else:
            app_id = self.app_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "url": url,
            }
        )
        if authorization_header is not UNSET:
            field_dict["authorization_header"] = authorization_header
        if environment is not UNSET:
            field_dict["environment"] = environment
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if app_id is not UNSET:
            field_dict["app_id"] = app_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        def _parse_authorization_header(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorization_header = _parse_authorization_header(d.pop("authorization_header", UNSET))

        def _parse_environment(
            data: object,
        ) -> (
            CreateWebhookIntegrationInputEnvironmentType1
            | CreateWebhookIntegrationInputEnvironmentType2Type1
            | CreateWebhookIntegrationInputEnvironmentType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_type_1 = CreateWebhookIntegrationInputEnvironmentType1(data)

                return environment_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_type_2_type_1 = CreateWebhookIntegrationInputEnvironmentType2Type1(data)

                return environment_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_type_3_type_1 = CreateWebhookIntegrationInputEnvironmentType3Type1(data)

                return environment_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateWebhookIntegrationInputEnvironmentType1
                | CreateWebhookIntegrationInputEnvironmentType2Type1
                | CreateWebhookIntegrationInputEnvironmentType3Type1
                | None
                | Unset,
                data,
            )

        environment = _parse_environment(d.pop("environment", UNSET))

        def _parse_event_types(data: object) -> list[WebhookEventType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = []
                _event_types_type_0 = data
                for event_types_type_0_item_data in _event_types_type_0:
                    event_types_type_0_item = WebhookEventType(event_types_type_0_item_data)

                    event_types_type_0.append(event_types_type_0_item)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WebhookEventType] | None | Unset, data)

        event_types = _parse_event_types(d.pop("event_types", UNSET))

        def _parse_app_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_id = _parse_app_id(d.pop("app_id", UNSET))

        create_webhook_integration_input = cls(
            name=name,
            url=url,
            authorization_header=authorization_header,
            environment=environment,
            event_types=event_types,
            app_id=app_id,
        )

        create_webhook_integration_input.additional_properties = d
        return create_webhook_integration_input

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
