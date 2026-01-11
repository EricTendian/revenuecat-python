from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_entitlement_response_400 import DeleteEntitlementResponse400
from ...models.delete_entitlement_response_401 import DeleteEntitlementResponse401
from ...models.delete_entitlement_response_403 import DeleteEntitlementResponse403
from ...models.delete_entitlement_response_404 import DeleteEntitlementResponse404
from ...models.delete_entitlement_response_409 import DeleteEntitlementResponse409
from ...models.delete_entitlement_response_422 import DeleteEntitlementResponse422
from ...models.delete_entitlement_response_423 import DeleteEntitlementResponse423
from ...models.delete_entitlement_response_429 import DeleteEntitlementResponse429
from ...models.delete_entitlement_response_500 import DeleteEntitlementResponse500
from ...models.delete_entitlement_response_503 import DeleteEntitlementResponse503
from ...models.deleted_object import DeletedObject
from ...types import Response


def _get_kwargs(
    project_id: str,
    entitlement_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/entitlements/{entitlement_id}".format(
            project_id=quote(str(project_id), safe=""),
            entitlement_id=quote(str(entitlement_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteEntitlementResponse400
    | DeleteEntitlementResponse401
    | DeleteEntitlementResponse403
    | DeleteEntitlementResponse404
    | DeleteEntitlementResponse409
    | DeleteEntitlementResponse422
    | DeleteEntitlementResponse423
    | DeleteEntitlementResponse429
    | DeleteEntitlementResponse500
    | DeleteEntitlementResponse503
    | DeletedObject
    | None
):
    if response.status_code == 200:
        response_200 = DeletedObject.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteEntitlementResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteEntitlementResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteEntitlementResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteEntitlementResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeleteEntitlementResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = DeleteEntitlementResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = DeleteEntitlementResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = DeleteEntitlementResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteEntitlementResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteEntitlementResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteEntitlementResponse400
    | DeleteEntitlementResponse401
    | DeleteEntitlementResponse403
    | DeleteEntitlementResponse404
    | DeleteEntitlementResponse409
    | DeleteEntitlementResponse422
    | DeleteEntitlementResponse423
    | DeleteEntitlementResponse429
    | DeleteEntitlementResponse500
    | DeleteEntitlementResponse503
    | DeletedObject
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
) -> Response[
    DeleteEntitlementResponse400
    | DeleteEntitlementResponse401
    | DeleteEntitlementResponse403
    | DeleteEntitlementResponse404
    | DeleteEntitlementResponse409
    | DeleteEntitlementResponse422
    | DeleteEntitlementResponse423
    | DeleteEntitlementResponse429
    | DeleteEntitlementResponse500
    | DeleteEntitlementResponse503
    | DeletedObject
]:
    """Delete an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEntitlementResponse400 | DeleteEntitlementResponse401 | DeleteEntitlementResponse403 | DeleteEntitlementResponse404 | DeleteEntitlementResponse409 | DeleteEntitlementResponse422 | DeleteEntitlementResponse423 | DeleteEntitlementResponse429 | DeleteEntitlementResponse500 | DeleteEntitlementResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        entitlement_id=entitlement_id,
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
) -> (
    DeleteEntitlementResponse400
    | DeleteEntitlementResponse401
    | DeleteEntitlementResponse403
    | DeleteEntitlementResponse404
    | DeleteEntitlementResponse409
    | DeleteEntitlementResponse422
    | DeleteEntitlementResponse423
    | DeleteEntitlementResponse429
    | DeleteEntitlementResponse500
    | DeleteEntitlementResponse503
    | DeletedObject
    | None
):
    """Delete an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEntitlementResponse400 | DeleteEntitlementResponse401 | DeleteEntitlementResponse403 | DeleteEntitlementResponse404 | DeleteEntitlementResponse409 | DeleteEntitlementResponse422 | DeleteEntitlementResponse423 | DeleteEntitlementResponse429 | DeleteEntitlementResponse500 | DeleteEntitlementResponse503 | DeletedObject
    """

    return sync_detailed(
        project_id=project_id,
        entitlement_id=entitlement_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteEntitlementResponse400
    | DeleteEntitlementResponse401
    | DeleteEntitlementResponse403
    | DeleteEntitlementResponse404
    | DeleteEntitlementResponse409
    | DeleteEntitlementResponse422
    | DeleteEntitlementResponse423
    | DeleteEntitlementResponse429
    | DeleteEntitlementResponse500
    | DeleteEntitlementResponse503
    | DeletedObject
]:
    """Delete an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEntitlementResponse400 | DeleteEntitlementResponse401 | DeleteEntitlementResponse403 | DeleteEntitlementResponse404 | DeleteEntitlementResponse409 | DeleteEntitlementResponse422 | DeleteEntitlementResponse423 | DeleteEntitlementResponse429 | DeleteEntitlementResponse500 | DeleteEntitlementResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        entitlement_id=entitlement_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteEntitlementResponse400
    | DeleteEntitlementResponse401
    | DeleteEntitlementResponse403
    | DeleteEntitlementResponse404
    | DeleteEntitlementResponse409
    | DeleteEntitlementResponse422
    | DeleteEntitlementResponse423
    | DeleteEntitlementResponse429
    | DeleteEntitlementResponse500
    | DeleteEntitlementResponse503
    | DeletedObject
    | None
):
    """Delete an entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEntitlementResponse400 | DeleteEntitlementResponse401 | DeleteEntitlementResponse403 | DeleteEntitlementResponse404 | DeleteEntitlementResponse409 | DeleteEntitlementResponse422 | DeleteEntitlementResponse423 | DeleteEntitlementResponse429 | DeleteEntitlementResponse500 | DeleteEntitlementResponse503 | DeletedObject
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            entitlement_id=entitlement_id,
            client=client,
        )
    ).parsed
