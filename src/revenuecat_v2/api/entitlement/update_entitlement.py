from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entitlement import Entitlement
from ...models.update_entitlement_body import UpdateEntitlementBody
from ...models.update_entitlement_response_400 import UpdateEntitlementResponse400
from ...models.update_entitlement_response_401 import UpdateEntitlementResponse401
from ...models.update_entitlement_response_403 import UpdateEntitlementResponse403
from ...models.update_entitlement_response_404 import UpdateEntitlementResponse404
from ...models.update_entitlement_response_409 import UpdateEntitlementResponse409
from ...models.update_entitlement_response_422 import UpdateEntitlementResponse422
from ...models.update_entitlement_response_423 import UpdateEntitlementResponse423
from ...models.update_entitlement_response_429 import UpdateEntitlementResponse429
from ...models.update_entitlement_response_500 import UpdateEntitlementResponse500
from ...models.update_entitlement_response_503 import UpdateEntitlementResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    entitlement_id: str,
    *,
    body: UpdateEntitlementBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/entitlements/{entitlement_id}".format(
            project_id=quote(str(project_id), safe=""),
            entitlement_id=quote(str(entitlement_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Entitlement
    | UpdateEntitlementResponse400
    | UpdateEntitlementResponse401
    | UpdateEntitlementResponse403
    | UpdateEntitlementResponse404
    | UpdateEntitlementResponse409
    | UpdateEntitlementResponse422
    | UpdateEntitlementResponse423
    | UpdateEntitlementResponse429
    | UpdateEntitlementResponse500
    | UpdateEntitlementResponse503
    | None
):
    if response.status_code == 200:
        response_200 = Entitlement.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateEntitlementResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateEntitlementResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdateEntitlementResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateEntitlementResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdateEntitlementResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = UpdateEntitlementResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = UpdateEntitlementResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = UpdateEntitlementResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateEntitlementResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateEntitlementResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Entitlement
    | UpdateEntitlementResponse400
    | UpdateEntitlementResponse401
    | UpdateEntitlementResponse403
    | UpdateEntitlementResponse404
    | UpdateEntitlementResponse409
    | UpdateEntitlementResponse422
    | UpdateEntitlementResponse423
    | UpdateEntitlementResponse429
    | UpdateEntitlementResponse500
    | UpdateEntitlementResponse503
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
    body: UpdateEntitlementBody,
) -> Response[
    Entitlement
    | UpdateEntitlementResponse400
    | UpdateEntitlementResponse401
    | UpdateEntitlementResponse403
    | UpdateEntitlementResponse404
    | UpdateEntitlementResponse409
    | UpdateEntitlementResponse422
    | UpdateEntitlementResponse423
    | UpdateEntitlementResponse429
    | UpdateEntitlementResponse500
    | UpdateEntitlementResponse503
]:
    """Update an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        body (UpdateEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Entitlement | UpdateEntitlementResponse400 | UpdateEntitlementResponse401 | UpdateEntitlementResponse403 | UpdateEntitlementResponse404 | UpdateEntitlementResponse409 | UpdateEntitlementResponse422 | UpdateEntitlementResponse423 | UpdateEntitlementResponse429 | UpdateEntitlementResponse500 | UpdateEntitlementResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        entitlement_id=entitlement_id,
        body=body,
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
    body: UpdateEntitlementBody,
) -> (
    Entitlement
    | UpdateEntitlementResponse400
    | UpdateEntitlementResponse401
    | UpdateEntitlementResponse403
    | UpdateEntitlementResponse404
    | UpdateEntitlementResponse409
    | UpdateEntitlementResponse422
    | UpdateEntitlementResponse423
    | UpdateEntitlementResponse429
    | UpdateEntitlementResponse500
    | UpdateEntitlementResponse503
    | None
):
    """Update an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        body (UpdateEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Entitlement | UpdateEntitlementResponse400 | UpdateEntitlementResponse401 | UpdateEntitlementResponse403 | UpdateEntitlementResponse404 | UpdateEntitlementResponse409 | UpdateEntitlementResponse422 | UpdateEntitlementResponse423 | UpdateEntitlementResponse429 | UpdateEntitlementResponse500 | UpdateEntitlementResponse503
    """

    return sync_detailed(
        project_id=project_id,
        entitlement_id=entitlement_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEntitlementBody,
) -> Response[
    Entitlement
    | UpdateEntitlementResponse400
    | UpdateEntitlementResponse401
    | UpdateEntitlementResponse403
    | UpdateEntitlementResponse404
    | UpdateEntitlementResponse409
    | UpdateEntitlementResponse422
    | UpdateEntitlementResponse423
    | UpdateEntitlementResponse429
    | UpdateEntitlementResponse500
    | UpdateEntitlementResponse503
]:
    """Update an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        body (UpdateEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Entitlement | UpdateEntitlementResponse400 | UpdateEntitlementResponse401 | UpdateEntitlementResponse403 | UpdateEntitlementResponse404 | UpdateEntitlementResponse409 | UpdateEntitlementResponse422 | UpdateEntitlementResponse423 | UpdateEntitlementResponse429 | UpdateEntitlementResponse500 | UpdateEntitlementResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        entitlement_id=entitlement_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEntitlementBody,
) -> (
    Entitlement
    | UpdateEntitlementResponse400
    | UpdateEntitlementResponse401
    | UpdateEntitlementResponse403
    | UpdateEntitlementResponse404
    | UpdateEntitlementResponse409
    | UpdateEntitlementResponse422
    | UpdateEntitlementResponse423
    | UpdateEntitlementResponse429
    | UpdateEntitlementResponse500
    | UpdateEntitlementResponse503
    | None
):
    """Update an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        body (UpdateEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Entitlement | UpdateEntitlementResponse400 | UpdateEntitlementResponse401 | UpdateEntitlementResponse403 | UpdateEntitlementResponse404 | UpdateEntitlementResponse409 | UpdateEntitlementResponse422 | UpdateEntitlementResponse423 | UpdateEntitlementResponse429 | UpdateEntitlementResponse500 | UpdateEntitlementResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            entitlement_id=entitlement_id,
            client=client,
            body=body,
        )
    ).parsed
