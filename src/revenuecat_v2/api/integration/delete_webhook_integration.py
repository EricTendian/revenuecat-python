from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_webhook_integration_response_400 import DeleteWebhookIntegrationResponse400
from ...models.delete_webhook_integration_response_401 import DeleteWebhookIntegrationResponse401
from ...models.delete_webhook_integration_response_403 import DeleteWebhookIntegrationResponse403
from ...models.delete_webhook_integration_response_404 import DeleteWebhookIntegrationResponse404
from ...models.delete_webhook_integration_response_409 import DeleteWebhookIntegrationResponse409
from ...models.delete_webhook_integration_response_422 import DeleteWebhookIntegrationResponse422
from ...models.delete_webhook_integration_response_423 import DeleteWebhookIntegrationResponse423
from ...models.delete_webhook_integration_response_429 import DeleteWebhookIntegrationResponse429
from ...models.delete_webhook_integration_response_500 import DeleteWebhookIntegrationResponse500
from ...models.delete_webhook_integration_response_503 import DeleteWebhookIntegrationResponse503
from ...models.deleted_object import DeletedObject
from ...types import Response


def _get_kwargs(
    project_id: str,
    webhook_integration_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/integrations/webhooks/{webhook_integration_id}".format(
            project_id=quote(str(project_id), safe=""),
            webhook_integration_id=quote(str(webhook_integration_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteWebhookIntegrationResponse400
    | DeleteWebhookIntegrationResponse401
    | DeleteWebhookIntegrationResponse403
    | DeleteWebhookIntegrationResponse404
    | DeleteWebhookIntegrationResponse409
    | DeleteWebhookIntegrationResponse422
    | DeleteWebhookIntegrationResponse423
    | DeleteWebhookIntegrationResponse429
    | DeleteWebhookIntegrationResponse500
    | DeleteWebhookIntegrationResponse503
    | DeletedObject
    | None
):
    if response.status_code == 200:
        response_200 = DeletedObject.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteWebhookIntegrationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteWebhookIntegrationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteWebhookIntegrationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteWebhookIntegrationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeleteWebhookIntegrationResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = DeleteWebhookIntegrationResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = DeleteWebhookIntegrationResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = DeleteWebhookIntegrationResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteWebhookIntegrationResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteWebhookIntegrationResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteWebhookIntegrationResponse400
    | DeleteWebhookIntegrationResponse401
    | DeleteWebhookIntegrationResponse403
    | DeleteWebhookIntegrationResponse404
    | DeleteWebhookIntegrationResponse409
    | DeleteWebhookIntegrationResponse422
    | DeleteWebhookIntegrationResponse423
    | DeleteWebhookIntegrationResponse429
    | DeleteWebhookIntegrationResponse500
    | DeleteWebhookIntegrationResponse503
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
    webhook_integration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteWebhookIntegrationResponse400
    | DeleteWebhookIntegrationResponse401
    | DeleteWebhookIntegrationResponse403
    | DeleteWebhookIntegrationResponse404
    | DeleteWebhookIntegrationResponse409
    | DeleteWebhookIntegrationResponse422
    | DeleteWebhookIntegrationResponse423
    | DeleteWebhookIntegrationResponse429
    | DeleteWebhookIntegrationResponse500
    | DeleteWebhookIntegrationResponse503
    | DeletedObject
]:
    """Delete a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWebhookIntegrationResponse400 | DeleteWebhookIntegrationResponse401 | DeleteWebhookIntegrationResponse403 | DeleteWebhookIntegrationResponse404 | DeleteWebhookIntegrationResponse409 | DeleteWebhookIntegrationResponse422 | DeleteWebhookIntegrationResponse423 | DeleteWebhookIntegrationResponse429 | DeleteWebhookIntegrationResponse500 | DeleteWebhookIntegrationResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        webhook_integration_id=webhook_integration_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    webhook_integration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteWebhookIntegrationResponse400
    | DeleteWebhookIntegrationResponse401
    | DeleteWebhookIntegrationResponse403
    | DeleteWebhookIntegrationResponse404
    | DeleteWebhookIntegrationResponse409
    | DeleteWebhookIntegrationResponse422
    | DeleteWebhookIntegrationResponse423
    | DeleteWebhookIntegrationResponse429
    | DeleteWebhookIntegrationResponse500
    | DeleteWebhookIntegrationResponse503
    | DeletedObject
    | None
):
    """Delete a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWebhookIntegrationResponse400 | DeleteWebhookIntegrationResponse401 | DeleteWebhookIntegrationResponse403 | DeleteWebhookIntegrationResponse404 | DeleteWebhookIntegrationResponse409 | DeleteWebhookIntegrationResponse422 | DeleteWebhookIntegrationResponse423 | DeleteWebhookIntegrationResponse429 | DeleteWebhookIntegrationResponse500 | DeleteWebhookIntegrationResponse503 | DeletedObject
    """

    return sync_detailed(
        project_id=project_id,
        webhook_integration_id=webhook_integration_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    webhook_integration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteWebhookIntegrationResponse400
    | DeleteWebhookIntegrationResponse401
    | DeleteWebhookIntegrationResponse403
    | DeleteWebhookIntegrationResponse404
    | DeleteWebhookIntegrationResponse409
    | DeleteWebhookIntegrationResponse422
    | DeleteWebhookIntegrationResponse423
    | DeleteWebhookIntegrationResponse429
    | DeleteWebhookIntegrationResponse500
    | DeleteWebhookIntegrationResponse503
    | DeletedObject
]:
    """Delete a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWebhookIntegrationResponse400 | DeleteWebhookIntegrationResponse401 | DeleteWebhookIntegrationResponse403 | DeleteWebhookIntegrationResponse404 | DeleteWebhookIntegrationResponse409 | DeleteWebhookIntegrationResponse422 | DeleteWebhookIntegrationResponse423 | DeleteWebhookIntegrationResponse429 | DeleteWebhookIntegrationResponse500 | DeleteWebhookIntegrationResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        webhook_integration_id=webhook_integration_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    webhook_integration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteWebhookIntegrationResponse400
    | DeleteWebhookIntegrationResponse401
    | DeleteWebhookIntegrationResponse403
    | DeleteWebhookIntegrationResponse404
    | DeleteWebhookIntegrationResponse409
    | DeleteWebhookIntegrationResponse422
    | DeleteWebhookIntegrationResponse423
    | DeleteWebhookIntegrationResponse429
    | DeleteWebhookIntegrationResponse500
    | DeleteWebhookIntegrationResponse503
    | DeletedObject
    | None
):
    """Delete a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWebhookIntegrationResponse400 | DeleteWebhookIntegrationResponse401 | DeleteWebhookIntegrationResponse403 | DeleteWebhookIntegrationResponse404 | DeleteWebhookIntegrationResponse409 | DeleteWebhookIntegrationResponse422 | DeleteWebhookIntegrationResponse423 | DeleteWebhookIntegrationResponse429 | DeleteWebhookIntegrationResponse500 | DeleteWebhookIntegrationResponse503 | DeletedObject
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            webhook_integration_id=webhook_integration_id,
            client=client,
        )
    ).parsed
