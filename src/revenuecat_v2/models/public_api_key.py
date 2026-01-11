from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.public_api_key_environment import PublicApiKeyEnvironment
from ..models.public_api_key_object import PublicApiKeyObject

T = TypeVar("T", bound="PublicApiKey")


@_attrs_define
class PublicApiKey:
    """
    Attributes:
        object_ (PublicApiKeyObject): String representing the object's type. Objects of the same type share the same
            value.
        id (str): The ID of the public API key Example: apikey12345.
        key (str): The value of the public API key Example: goog_1ab2c3d4.
        environment (PublicApiKeyEnvironment): The environment the public API key is for
        app_id (str): The ID of the app the public API key is for Example: app1a2b3c4.
        created_at (int): The date when the public API key was created in ms since epoch Example: 1658399423658.
    """

    object_: PublicApiKeyObject
    id: str
    key: str
    environment: PublicApiKeyEnvironment
    app_id: str
    created_at: int

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        key = self.key

        environment = self.environment.value

        app_id = self.app_id

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "key": key,
                "environment": environment,
                "app_id": app_id,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = PublicApiKeyObject(d.pop("object"))

        id = d.pop("id")

        key = d.pop("key")

        environment = PublicApiKeyEnvironment(d.pop("environment"))

        app_id = d.pop("app_id")

        created_at = d.pop("created_at")

        public_api_key = cls(
            object_=object_,
            id=id,
            key=key,
            environment=environment,
            app_id=app_id,
            created_at=created_at,
        )

        return public_api_key
