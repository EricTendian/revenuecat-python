from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_entitlement_body import CreateEntitlementBody
from ...models.create_entitlement_response_400 import CreateEntitlementResponse400
from ...models.create_entitlement_response_401 import CreateEntitlementResponse401
from ...models.create_entitlement_response_403 import CreateEntitlementResponse403
from ...models.create_entitlement_response_404 import CreateEntitlementResponse404
from ...models.create_entitlement_response_409 import CreateEntitlementResponse409
from ...models.create_entitlement_response_422 import CreateEntitlementResponse422
from ...models.create_entitlement_response_423 import CreateEntitlementResponse423
from ...models.create_entitlement_response_429 import CreateEntitlementResponse429
from ...models.create_entitlement_response_500 import CreateEntitlementResponse500
from ...models.create_entitlement_response_503 import CreateEntitlementResponse503
from ...models.entitlement import Entitlement
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: CreateEntitlementBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/entitlements".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateEntitlementResponse400
    | CreateEntitlementResponse401
    | CreateEntitlementResponse403
    | CreateEntitlementResponse404
    | CreateEntitlementResponse409
    | CreateEntitlementResponse422
    | CreateEntitlementResponse423
    | CreateEntitlementResponse429
    | CreateEntitlementResponse500
    | CreateEntitlementResponse503
    | Entitlement
    | None
):
    if response.status_code == 201:
        response_201 = Entitlement.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateEntitlementResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateEntitlementResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreateEntitlementResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateEntitlementResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreateEntitlementResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CreateEntitlementResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = CreateEntitlementResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = CreateEntitlementResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateEntitlementResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateEntitlementResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateEntitlementResponse400
    | CreateEntitlementResponse401
    | CreateEntitlementResponse403
    | CreateEntitlementResponse404
    | CreateEntitlementResponse409
    | CreateEntitlementResponse422
    | CreateEntitlementResponse423
    | CreateEntitlementResponse429
    | CreateEntitlementResponse500
    | CreateEntitlementResponse503
    | Entitlement
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEntitlementBody,
) -> Response[
    CreateEntitlementResponse400
    | CreateEntitlementResponse401
    | CreateEntitlementResponse403
    | CreateEntitlementResponse404
    | CreateEntitlementResponse409
    | CreateEntitlementResponse422
    | CreateEntitlementResponse423
    | CreateEntitlementResponse429
    | CreateEntitlementResponse500
    | CreateEntitlementResponse503
    | Entitlement
]:
    """Create an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEntitlementResponse400 | CreateEntitlementResponse401 | CreateEntitlementResponse403 | CreateEntitlementResponse404 | CreateEntitlementResponse409 | CreateEntitlementResponse422 | CreateEntitlementResponse423 | CreateEntitlementResponse429 | CreateEntitlementResponse500 | CreateEntitlementResponse503 | Entitlement]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEntitlementBody,
) -> (
    CreateEntitlementResponse400
    | CreateEntitlementResponse401
    | CreateEntitlementResponse403
    | CreateEntitlementResponse404
    | CreateEntitlementResponse409
    | CreateEntitlementResponse422
    | CreateEntitlementResponse423
    | CreateEntitlementResponse429
    | CreateEntitlementResponse500
    | CreateEntitlementResponse503
    | Entitlement
    | None
):
    """Create an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEntitlementResponse400 | CreateEntitlementResponse401 | CreateEntitlementResponse403 | CreateEntitlementResponse404 | CreateEntitlementResponse409 | CreateEntitlementResponse422 | CreateEntitlementResponse423 | CreateEntitlementResponse429 | CreateEntitlementResponse500 | CreateEntitlementResponse503 | Entitlement
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEntitlementBody,
) -> Response[
    CreateEntitlementResponse400
    | CreateEntitlementResponse401
    | CreateEntitlementResponse403
    | CreateEntitlementResponse404
    | CreateEntitlementResponse409
    | CreateEntitlementResponse422
    | CreateEntitlementResponse423
    | CreateEntitlementResponse429
    | CreateEntitlementResponse500
    | CreateEntitlementResponse503
    | Entitlement
]:
    """Create an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEntitlementResponse400 | CreateEntitlementResponse401 | CreateEntitlementResponse403 | CreateEntitlementResponse404 | CreateEntitlementResponse409 | CreateEntitlementResponse422 | CreateEntitlementResponse423 | CreateEntitlementResponse429 | CreateEntitlementResponse500 | CreateEntitlementResponse503 | Entitlement]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEntitlementBody,
) -> (
    CreateEntitlementResponse400
    | CreateEntitlementResponse401
    | CreateEntitlementResponse403
    | CreateEntitlementResponse404
    | CreateEntitlementResponse409
    | CreateEntitlementResponse422
    | CreateEntitlementResponse423
    | CreateEntitlementResponse429
    | CreateEntitlementResponse500
    | CreateEntitlementResponse503
    | Entitlement
    | None
):
    """Create an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEntitlementResponse400 | CreateEntitlementResponse401 | CreateEntitlementResponse403 | CreateEntitlementResponse404 | CreateEntitlementResponse409 | CreateEntitlementResponse422 | CreateEntitlementResponse423 | CreateEntitlementResponse429 | CreateEntitlementResponse500 | CreateEntitlementResponse503 | Entitlement
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
