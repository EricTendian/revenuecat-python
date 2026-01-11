from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_webhook_integration_input import CreateWebhookIntegrationInput
from ...models.create_webhook_integration_response_400 import CreateWebhookIntegrationResponse400
from ...models.create_webhook_integration_response_401 import CreateWebhookIntegrationResponse401
from ...models.create_webhook_integration_response_403 import CreateWebhookIntegrationResponse403
from ...models.create_webhook_integration_response_404 import CreateWebhookIntegrationResponse404
from ...models.create_webhook_integration_response_409 import CreateWebhookIntegrationResponse409
from ...models.create_webhook_integration_response_422 import CreateWebhookIntegrationResponse422
from ...models.create_webhook_integration_response_423 import CreateWebhookIntegrationResponse423
from ...models.create_webhook_integration_response_429 import CreateWebhookIntegrationResponse429
from ...models.create_webhook_integration_response_500 import CreateWebhookIntegrationResponse500
from ...models.create_webhook_integration_response_503 import CreateWebhookIntegrationResponse503
from ...models.webhook_integration import WebhookIntegration
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: CreateWebhookIntegrationInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/integrations/webhooks".format(
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
    CreateWebhookIntegrationResponse400
    | CreateWebhookIntegrationResponse401
    | CreateWebhookIntegrationResponse403
    | CreateWebhookIntegrationResponse404
    | CreateWebhookIntegrationResponse409
    | CreateWebhookIntegrationResponse422
    | CreateWebhookIntegrationResponse423
    | CreateWebhookIntegrationResponse429
    | CreateWebhookIntegrationResponse500
    | CreateWebhookIntegrationResponse503
    | WebhookIntegration
    | None
):
    if response.status_code == 201:
        response_201 = WebhookIntegration.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateWebhookIntegrationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateWebhookIntegrationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreateWebhookIntegrationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateWebhookIntegrationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreateWebhookIntegrationResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CreateWebhookIntegrationResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = CreateWebhookIntegrationResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = CreateWebhookIntegrationResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateWebhookIntegrationResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateWebhookIntegrationResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateWebhookIntegrationResponse400
    | CreateWebhookIntegrationResponse401
    | CreateWebhookIntegrationResponse403
    | CreateWebhookIntegrationResponse404
    | CreateWebhookIntegrationResponse409
    | CreateWebhookIntegrationResponse422
    | CreateWebhookIntegrationResponse423
    | CreateWebhookIntegrationResponse429
    | CreateWebhookIntegrationResponse500
    | CreateWebhookIntegrationResponse503
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
    *,
    client: AuthenticatedClient | Client,
    body: CreateWebhookIntegrationInput,
) -> Response[
    CreateWebhookIntegrationResponse400
    | CreateWebhookIntegrationResponse401
    | CreateWebhookIntegrationResponse403
    | CreateWebhookIntegrationResponse404
    | CreateWebhookIntegrationResponse409
    | CreateWebhookIntegrationResponse422
    | CreateWebhookIntegrationResponse423
    | CreateWebhookIntegrationResponse429
    | CreateWebhookIntegrationResponse500
    | CreateWebhookIntegrationResponse503
    | WebhookIntegration
]:
    """Create a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateWebhookIntegrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookIntegrationResponse400 | CreateWebhookIntegrationResponse401 | CreateWebhookIntegrationResponse403 | CreateWebhookIntegrationResponse404 | CreateWebhookIntegrationResponse409 | CreateWebhookIntegrationResponse422 | CreateWebhookIntegrationResponse423 | CreateWebhookIntegrationResponse429 | CreateWebhookIntegrationResponse500 | CreateWebhookIntegrationResponse503 | WebhookIntegration]
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
    body: CreateWebhookIntegrationInput,
) -> (
    CreateWebhookIntegrationResponse400
    | CreateWebhookIntegrationResponse401
    | CreateWebhookIntegrationResponse403
    | CreateWebhookIntegrationResponse404
    | CreateWebhookIntegrationResponse409
    | CreateWebhookIntegrationResponse422
    | CreateWebhookIntegrationResponse423
    | CreateWebhookIntegrationResponse429
    | CreateWebhookIntegrationResponse500
    | CreateWebhookIntegrationResponse503
    | WebhookIntegration
    | None
):
    """Create a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateWebhookIntegrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookIntegrationResponse400 | CreateWebhookIntegrationResponse401 | CreateWebhookIntegrationResponse403 | CreateWebhookIntegrationResponse404 | CreateWebhookIntegrationResponse409 | CreateWebhookIntegrationResponse422 | CreateWebhookIntegrationResponse423 | CreateWebhookIntegrationResponse429 | CreateWebhookIntegrationResponse500 | CreateWebhookIntegrationResponse503 | WebhookIntegration
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
    body: CreateWebhookIntegrationInput,
) -> Response[
    CreateWebhookIntegrationResponse400
    | CreateWebhookIntegrationResponse401
    | CreateWebhookIntegrationResponse403
    | CreateWebhookIntegrationResponse404
    | CreateWebhookIntegrationResponse409
    | CreateWebhookIntegrationResponse422
    | CreateWebhookIntegrationResponse423
    | CreateWebhookIntegrationResponse429
    | CreateWebhookIntegrationResponse500
    | CreateWebhookIntegrationResponse503
    | WebhookIntegration
]:
    """Create a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateWebhookIntegrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookIntegrationResponse400 | CreateWebhookIntegrationResponse401 | CreateWebhookIntegrationResponse403 | CreateWebhookIntegrationResponse404 | CreateWebhookIntegrationResponse409 | CreateWebhookIntegrationResponse422 | CreateWebhookIntegrationResponse423 | CreateWebhookIntegrationResponse429 | CreateWebhookIntegrationResponse500 | CreateWebhookIntegrationResponse503 | WebhookIntegration]
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
    body: CreateWebhookIntegrationInput,
) -> (
    CreateWebhookIntegrationResponse400
    | CreateWebhookIntegrationResponse401
    | CreateWebhookIntegrationResponse403
    | CreateWebhookIntegrationResponse404
    | CreateWebhookIntegrationResponse409
    | CreateWebhookIntegrationResponse422
    | CreateWebhookIntegrationResponse423
    | CreateWebhookIntegrationResponse429
    | CreateWebhookIntegrationResponse500
    | CreateWebhookIntegrationResponse503
    | WebhookIntegration
    | None
):
    """Create a webhook integration

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateWebhookIntegrationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookIntegrationResponse400 | CreateWebhookIntegrationResponse401 | CreateWebhookIntegrationResponse403 | CreateWebhookIntegrationResponse404 | CreateWebhookIntegrationResponse409 | CreateWebhookIntegrationResponse422 | CreateWebhookIntegrationResponse423 | CreateWebhookIntegrationResponse429 | CreateWebhookIntegrationResponse500 | CreateWebhookIntegrationResponse503 | WebhookIntegration
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
