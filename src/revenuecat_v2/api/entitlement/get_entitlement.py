from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entitlement import Entitlement
from ...models.get_entitlement_expand_item import GetEntitlementExpandItem
from ...models.get_entitlement_response_400 import GetEntitlementResponse400
from ...models.get_entitlement_response_401 import GetEntitlementResponse401
from ...models.get_entitlement_response_403 import GetEntitlementResponse403
from ...models.get_entitlement_response_404 import GetEntitlementResponse404
from ...models.get_entitlement_response_423 import GetEntitlementResponse423
from ...models.get_entitlement_response_429 import GetEntitlementResponse429
from ...models.get_entitlement_response_500 import GetEntitlementResponse500
from ...models.get_entitlement_response_503 import GetEntitlementResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    entitlement_id: str,
    *,
    expand: list[GetEntitlementExpandItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_expand: list[str] | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item = expand_item_data.value
            json_expand.append(expand_item)

    params["expand"] = json_expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/entitlements/{entitlement_id}".format(
            project_id=quote(str(project_id), safe=""),
            entitlement_id=quote(str(entitlement_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Entitlement
    | GetEntitlementResponse400
    | GetEntitlementResponse401
    | GetEntitlementResponse403
    | GetEntitlementResponse404
    | GetEntitlementResponse423
    | GetEntitlementResponse429
    | GetEntitlementResponse500
    | GetEntitlementResponse503
    | None
):
    if response.status_code == 200:
        response_200 = Entitlement.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetEntitlementResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetEntitlementResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetEntitlementResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetEntitlementResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetEntitlementResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetEntitlementResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetEntitlementResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetEntitlementResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Entitlement
    | GetEntitlementResponse400
    | GetEntitlementResponse401
    | GetEntitlementResponse403
    | GetEntitlementResponse404
    | GetEntitlementResponse423
    | GetEntitlementResponse429
    | GetEntitlementResponse500
    | GetEntitlementResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetEntitlementExpandItem] | Unset = UNSET,
) -> Response[
    Entitlement
    | GetEntitlementResponse400
    | GetEntitlementResponse401
    | GetEntitlementResponse403
    | GetEntitlementResponse404
    | GetEntitlementResponse423
    | GetEntitlementResponse429
    | GetEntitlementResponse500
    | GetEntitlementResponse503
]:
    """Get an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        expand (list[GetEntitlementExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Entitlement | GetEntitlementResponse400 | GetEntitlementResponse401 | GetEntitlementResponse403 | GetEntitlementResponse404 | GetEntitlementResponse423 | GetEntitlementResponse429 | GetEntitlementResponse500 | GetEntitlementResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        entitlement_id=entitlement_id,
        expand=expand,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetEntitlementExpandItem] | Unset = UNSET,
) -> (
    Entitlement
    | GetEntitlementResponse400
    | GetEntitlementResponse401
    | GetEntitlementResponse403
    | GetEntitlementResponse404
    | GetEntitlementResponse423
    | GetEntitlementResponse429
    | GetEntitlementResponse500
    | GetEntitlementResponse503
    | None
):
    """Get an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        expand (list[GetEntitlementExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Entitlement | GetEntitlementResponse400 | GetEntitlementResponse401 | GetEntitlementResponse403 | GetEntitlementResponse404 | GetEntitlementResponse423 | GetEntitlementResponse429 | GetEntitlementResponse500 | GetEntitlementResponse503
    """

    return sync_detailed(
        project_id=project_id,
        entitlement_id=entitlement_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetEntitlementExpandItem] | Unset = UNSET,
) -> Response[
    Entitlement
    | GetEntitlementResponse400
    | GetEntitlementResponse401
    | GetEntitlementResponse403
    | GetEntitlementResponse404
    | GetEntitlementResponse423
    | GetEntitlementResponse429
    | GetEntitlementResponse500
    | GetEntitlementResponse503
]:
    """Get an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        expand (list[GetEntitlementExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Entitlement | GetEntitlementResponse400 | GetEntitlementResponse401 | GetEntitlementResponse403 | GetEntitlementResponse404 | GetEntitlementResponse423 | GetEntitlementResponse429 | GetEntitlementResponse500 | GetEntitlementResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        entitlement_id=entitlement_id,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetEntitlementExpandItem] | Unset = UNSET,
) -> (
    Entitlement
    | GetEntitlementResponse400
    | GetEntitlementResponse401
    | GetEntitlementResponse403
    | GetEntitlementResponse404
    | GetEntitlementResponse423
    | GetEntitlementResponse429
    | GetEntitlementResponse500
    | GetEntitlementResponse503
    | None
):
    """Get an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        expand (list[GetEntitlementExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Entitlement | GetEntitlementResponse400 | GetEntitlementResponse401 | GetEntitlementResponse403 | GetEntitlementResponse404 | GetEntitlementResponse423 | GetEntitlementResponse429 | GetEntitlementResponse500 | GetEntitlementResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            entitlement_id=entitlement_id,
            client=client,
            expand=expand,
        )
    ).parsed
