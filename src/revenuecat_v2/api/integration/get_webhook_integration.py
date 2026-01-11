from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_webhook_integration_response_400 import GetWebhookIntegrationResponse400
from ...models.get_webhook_integration_response_401 import GetWebhookIntegrationResponse401
from ...models.get_webhook_integration_response_403 import GetWebhookIntegrationResponse403
from ...models.get_webhook_integration_response_404 import GetWebhookIntegrationResponse404
from ...models.get_webhook_integration_response_423 import GetWebhookIntegrationResponse423
from ...models.get_webhook_integration_response_429 import GetWebhookIntegrationResponse429
from ...models.get_webhook_integration_response_500 import GetWebhookIntegrationResponse500
from ...models.get_webhook_integration_response_503 import GetWebhookIntegrationResponse503
from ...models.webhook_integration import WebhookIntegration
from ...types import Response


def _get_kwargs(
    project_id: str,
    webhook_integration_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/integrations/webhooks/{webhook_integration_id}".format(
            project_id=quote(str(project_id), safe=""),
            webhook_integration_id=quote(str(webhook_integration_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetWebhookIntegrationResponse400
    | GetWebhookIntegrationResponse401
    | GetWebhookIntegrationResponse403
    | GetWebhookIntegrationResponse404
    | GetWebhookIntegrationResponse423
    | GetWebhookIntegrationResponse429
    | GetWebhookIntegrationResponse500
    | GetWebhookIntegrationResponse503
    | WebhookIntegration
    | None
):
    if response.status_code == 200:
        response_200 = WebhookIntegration.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetWebhookIntegrationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetWebhookIntegrationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetWebhookIntegrationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetWebhookIntegrationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetWebhookIntegrationResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetWebhookIntegrationResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetWebhookIntegrationResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetWebhookIntegrationResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetWebhookIntegrationResponse400
    | GetWebhookIntegrationResponse401
    | GetWebhookIntegrationResponse403
    | GetWebhookIntegrationResponse404
    | GetWebhookIntegrationResponse423
    | GetWebhookIntegrationResponse429
    | GetWebhookIntegrationResponse500
    | GetWebhookIntegrationResponse503
    | WebhookIntegration
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
    GetWebhookIntegrationResponse400
    | GetWebhookIntegrationResponse401
    | GetWebhookIntegrationResponse403
    | GetWebhookIntegrationResponse404
    | GetWebhookIntegrationResponse423
    | GetWebhookIntegrationResponse429
    | GetWebhookIntegrationResponse500
    | GetWebhookIntegrationResponse503
    | WebhookIntegration
]:
    """Get a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebhookIntegrationResponse400 | GetWebhookIntegrationResponse401 | GetWebhookIntegrationResponse403 | GetWebhookIntegrationResponse404 | GetWebhookIntegrationResponse423 | GetWebhookIntegrationResponse429 | GetWebhookIntegrationResponse500 | GetWebhookIntegrationResponse503 | WebhookIntegration]
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
    GetWebhookIntegrationResponse400
    | GetWebhookIntegrationResponse401
    | GetWebhookIntegrationResponse403
    | GetWebhookIntegrationResponse404
    | GetWebhookIntegrationResponse423
    | GetWebhookIntegrationResponse429
    | GetWebhookIntegrationResponse500
    | GetWebhookIntegrationResponse503
    | WebhookIntegration
    | None
):
    """Get a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebhookIntegrationResponse400 | GetWebhookIntegrationResponse401 | GetWebhookIntegrationResponse403 | GetWebhookIntegrationResponse404 | GetWebhookIntegrationResponse423 | GetWebhookIntegrationResponse429 | GetWebhookIntegrationResponse500 | GetWebhookIntegrationResponse503 | WebhookIntegration
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
    GetWebhookIntegrationResponse400
    | GetWebhookIntegrationResponse401
    | GetWebhookIntegrationResponse403
    | GetWebhookIntegrationResponse404
    | GetWebhookIntegrationResponse423
    | GetWebhookIntegrationResponse429
    | GetWebhookIntegrationResponse500
    | GetWebhookIntegrationResponse503
    | WebhookIntegration
]:
    """Get a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebhookIntegrationResponse400 | GetWebhookIntegrationResponse401 | GetWebhookIntegrationResponse403 | GetWebhookIntegrationResponse404 | GetWebhookIntegrationResponse423 | GetWebhookIntegrationResponse429 | GetWebhookIntegrationResponse500 | GetWebhookIntegrationResponse503 | WebhookIntegration]
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
    GetWebhookIntegrationResponse400
    | GetWebhookIntegrationResponse401
    | GetWebhookIntegrationResponse403
    | GetWebhookIntegrationResponse404
    | GetWebhookIntegrationResponse423
    | GetWebhookIntegrationResponse429
    | GetWebhookIntegrationResponse500
    | GetWebhookIntegrationResponse503
    | WebhookIntegration
    | None
):
    """Get a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebhookIntegrationResponse400 | GetWebhookIntegrationResponse401 | GetWebhookIntegrationResponse403 | GetWebhookIntegrationResponse404 | GetWebhookIntegrationResponse423 | GetWebhookIntegrationResponse429 | GetWebhookIntegrationResponse500 | GetWebhookIntegrationResponse503 | WebhookIntegration
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            webhook_integration_id=webhook_integration_id,
            client=client,
        )
    ).parsed
