from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_object import ErrorObject
from ..models.get_entitlement_response_404_type import GetEntitlementResponse404Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetEntitlementResponse404")


@_attrs_define
class GetEntitlementResponse404:
    """
    Example:
        {'object': 'error', 'type': 'resource_missing', 'message': 'Resource not found', 'retryable': False, 'doc_url':
            'https://errors.rev.cat/resource-missing'}

    Attributes:
        object_ (ErrorObject): String representing the object's type. Objects of the same type share the same value.
            Example: error.
        type_ (GetEntitlementResponse404Type): The error type Example: parameter_error.
        message (str): A message describing the reason of the error Example: id shouldn't be longer than 1,500
            characters.
        retryable (bool): Indicates if the error is retryable or not
        param (None | str | Unset): If the error is parameter-specific, the parameter related to the error Example:
            customer_id.
        doc_url (str | Unset): A URL to more information about the error reported Example:
            https://errors.rev.cat/parameter-error.
        backoff_ms (int | None | Unset): The ms the client should wait before retrying the request. Only present for
            retryable errors.
    """

    object_: ErrorObject
    type_: GetEntitlementResponse404Type
    message: str
    retryable: bool
    param: None | str | Unset = UNSET
    doc_url: str | Unset = UNSET
    backoff_ms: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        type_ = self.type_.value

        message = self.message

        retryable = self.retryable

        param: None | str | Unset
        if isinstance(self.param, Unset):
            param = UNSET
        else:
            param = self.param

        doc_url = self.doc_url

        backoff_ms: int | None | Unset
        if isinstance(self.backoff_ms, Unset):
            backoff_ms = UNSET
        else:
            backoff_ms = self.backoff_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "type": type_,
                "message": message,
                "retryable": retryable,
            }
        )
        if param is not UNSET:
            field_dict["param"] = param
        if doc_url is not UNSET:
            field_dict["doc_url"] = doc_url
        if backoff_ms is not UNSET:
            field_dict["backoff_ms"] = backoff_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = ErrorObject(d.pop("object"))

        type_ = GetEntitlementResponse404Type(d.pop("type"))

        message = d.pop("message")

        retryable = d.pop("retryable")

        def _parse_param(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        param = _parse_param(d.pop("param", UNSET))

        doc_url = d.pop("doc_url", UNSET)

        def _parse_backoff_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backoff_ms = _parse_backoff_ms(d.pop("backoff_ms", UNSET))

        get_entitlement_response_404 = cls(
            object_=object_,
            type_=type_,
            message=message,
            retryable=retryable,
            param=param,
            doc_url=doc_url,
            backoff_ms=backoff_ms,
        )

        get_entitlement_response_404.additional_properties = d
        return get_entitlement_response_404

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
