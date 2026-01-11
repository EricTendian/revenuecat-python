from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_webhook_integration_input import UpdateWebhookIntegrationInput
from ...models.update_webhook_integration_response_400 import UpdateWebhookIntegrationResponse400
from ...models.update_webhook_integration_response_401 import UpdateWebhookIntegrationResponse401
from ...models.update_webhook_integration_response_403 import UpdateWebhookIntegrationResponse403
from ...models.update_webhook_integration_response_404 import UpdateWebhookIntegrationResponse404
from ...models.update_webhook_integration_response_409 import UpdateWebhookIntegrationResponse409
from ...models.update_webhook_integration_response_422 import UpdateWebhookIntegrationResponse422
from ...models.update_webhook_integration_response_423 import UpdateWebhookIntegrationResponse423
from ...models.update_webhook_integration_response_429 import UpdateWebhookIntegrationResponse429
from ...models.update_webhook_integration_response_500 import UpdateWebhookIntegrationResponse500
from ...models.update_webhook_integration_response_503 import UpdateWebhookIntegrationResponse503
from ...models.webhook_integration import WebhookIntegration
from ...types import Response


def _get_kwargs(
    project_id: str,
    webhook_integration_id: str,
    *,
    body: UpdateWebhookIntegrationInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/integrations/webhooks/{webhook_integration_id}".format(
            project_id=quote(str(project_id), safe=""),
            webhook_integration_id=quote(str(webhook_integration_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateWebhookIntegrationResponse400
    | UpdateWebhookIntegrationResponse401
    | UpdateWebhookIntegrationResponse403
    | UpdateWebhookIntegrationResponse404
    | UpdateWebhookIntegrationResponse409
    | UpdateWebhookIntegrationResponse422
    | UpdateWebhookIntegrationResponse423
    | UpdateWebhookIntegrationResponse429
    | UpdateWebhookIntegrationResponse500
    | UpdateWebhookIntegrationResponse503
    | WebhookIntegration
    | None
):
    if response.status_code == 200:
        response_200 = WebhookIntegration.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateWebhookIntegrationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateWebhookIntegrationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdateWebhookIntegrationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateWebhookIntegrationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdateWebhookIntegrationResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = UpdateWebhookIntegrationResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = UpdateWebhookIntegrationResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = UpdateWebhookIntegrationResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateWebhookIntegrationResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateWebhookIntegrationResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateWebhookIntegrationResponse400
    | UpdateWebhookIntegrationResponse401
    | UpdateWebhookIntegrationResponse403
    | UpdateWebhookIntegrationResponse404
    | UpdateWebhookIntegrationResponse409
    | UpdateWebhookIntegrationResponse422
    | UpdateWebhookIntegrationResponse423
    | UpdateWebhookIntegrationResponse429
    | UpdateWebhookIntegrationResponse500
    | UpdateWebhookIntegrationResponse503
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
    body: UpdateWebhookIntegrationInput,
) -> Response[
    UpdateWebhookIntegrationResponse400
    | UpdateWebhookIntegrationResponse401
    | UpdateWebhookIntegrationResponse403
    | UpdateWebhookIntegrationResponse404
    | UpdateWebhookIntegrationResponse409
    | UpdateWebhookIntegrationResponse422
    | UpdateWebhookIntegrationResponse423
    | UpdateWebhookIntegrationResponse429
    | UpdateWebhookIntegrationResponse500
    | UpdateWebhookIntegrationResponse503
    | WebhookIntegration
]:
    """Update a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):
        body (UpdateWebhookIntegrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWebhookIntegrationResponse400 | UpdateWebhookIntegrationResponse401 | UpdateWebhookIntegrationResponse403 | UpdateWebhookIntegrationResponse404 | UpdateWebhookIntegrationResponse409 | UpdateWebhookIntegrationResponse422 | UpdateWebhookIntegrationResponse423 | UpdateWebhookIntegrationResponse429 | UpdateWebhookIntegrationResponse500 | UpdateWebhookIntegrationResponse503 | WebhookIntegration]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        webhook_integration_id=webhook_integration_id,
        body=body,
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
    body: UpdateWebhookIntegrationInput,
) -> (
    UpdateWebhookIntegrationResponse400
    | UpdateWebhookIntegrationResponse401
    | UpdateWebhookIntegrationResponse403
    | UpdateWebhookIntegrationResponse404
    | UpdateWebhookIntegrationResponse409
    | UpdateWebhookIntegrationResponse422
    | UpdateWebhookIntegrationResponse423
    | UpdateWebhookIntegrationResponse429
    | UpdateWebhookIntegrationResponse500
    | UpdateWebhookIntegrationResponse503
    | WebhookIntegration
    | None
):
    """Update a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):
        body (UpdateWebhookIntegrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWebhookIntegrationResponse400 | UpdateWebhookIntegrationResponse401 | UpdateWebhookIntegrationResponse403 | UpdateWebhookIntegrationResponse404 | UpdateWebhookIntegrationResponse409 | UpdateWebhookIntegrationResponse422 | UpdateWebhookIntegrationResponse423 | UpdateWebhookIntegrationResponse429 | UpdateWebhookIntegrationResponse500 | UpdateWebhookIntegrationResponse503 | WebhookIntegration
    """

    return sync_detailed(
        project_id=project_id,
        webhook_integration_id=webhook_integration_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    webhook_integration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookIntegrationInput,
) -> Response[
    UpdateWebhookIntegrationResponse400
    | UpdateWebhookIntegrationResponse401
    | UpdateWebhookIntegrationResponse403
    | UpdateWebhookIntegrationResponse404
    | UpdateWebhookIntegrationResponse409
    | UpdateWebhookIntegrationResponse422
    | UpdateWebhookIntegrationResponse423
    | UpdateWebhookIntegrationResponse429
    | UpdateWebhookIntegrationResponse500
    | UpdateWebhookIntegrationResponse503
    | WebhookIntegration
]:
    """Update a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):
        body (UpdateWebhookIntegrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWebhookIntegrationResponse400 | UpdateWebhookIntegrationResponse401 | UpdateWebhookIntegrationResponse403 | UpdateWebhookIntegrationResponse404 | UpdateWebhookIntegrationResponse409 | UpdateWebhookIntegrationResponse422 | UpdateWebhookIntegrationResponse423 | UpdateWebhookIntegrationResponse429 | UpdateWebhookIntegrationResponse500 | UpdateWebhookIntegrationResponse503 | WebhookIntegration]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        webhook_integration_id=webhook_integration_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    webhook_integration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookIntegrationInput,
) -> (
    UpdateWebhookIntegrationResponse400
    | UpdateWebhookIntegrationResponse401
    | UpdateWebhookIntegrationResponse403
    | UpdateWebhookIntegrationResponse404
    | UpdateWebhookIntegrationResponse409
    | UpdateWebhookIntegrationResponse422
    | UpdateWebhookIntegrationResponse423
    | UpdateWebhookIntegrationResponse429
    | UpdateWebhookIntegrationResponse500
    | UpdateWebhookIntegrationResponse503
    | WebhookIntegration
    | None
):
    """Update a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        webhook_integration_id (str):
        body (UpdateWebhookIntegrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWebhookIntegrationResponse400 | UpdateWebhookIntegrationResponse401 | UpdateWebhookIntegrationResponse403 | UpdateWebhookIntegrationResponse404 | UpdateWebhookIntegrationResponse409 | UpdateWebhookIntegrationResponse422 | UpdateWebhookIntegrationResponse423 | UpdateWebhookIntegrationResponse429 | UpdateWebhookIntegrationResponse500 | UpdateWebhookIntegrationResponse503 | WebhookIntegration
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            webhook_integration_id=webhook_integration_id,
            client=client,
            body=body,
        )
    ).parsed
