from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_webhook_integrations_response_400 import ListWebhookIntegrationsResponse400
from ...models.list_webhook_integrations_response_401 import ListWebhookIntegrationsResponse401
from ...models.list_webhook_integrations_response_403 import ListWebhookIntegrationsResponse403
from ...models.list_webhook_integrations_response_404 import ListWebhookIntegrationsResponse404
from ...models.list_webhook_integrations_response_423 import ListWebhookIntegrationsResponse423
from ...models.list_webhook_integrations_response_429 import ListWebhookIntegrationsResponse429
from ...models.list_webhook_integrations_response_500 import ListWebhookIntegrationsResponse500
from ...models.list_webhook_integrations_response_503 import ListWebhookIntegrationsResponse503
from ...models.webhook_integration_list import WebhookIntegrationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["starting_after"] = starting_after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/integrations/webhooks".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListWebhookIntegrationsResponse400
    | ListWebhookIntegrationsResponse401
    | ListWebhookIntegrationsResponse403
    | ListWebhookIntegrationsResponse404
    | ListWebhookIntegrationsResponse423
    | ListWebhookIntegrationsResponse429
    | ListWebhookIntegrationsResponse500
    | ListWebhookIntegrationsResponse503
    | WebhookIntegrationList
    | None
):
    if response.status_code == 200:
        response_200 = WebhookIntegrationList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListWebhookIntegrationsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListWebhookIntegrationsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListWebhookIntegrationsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListWebhookIntegrationsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListWebhookIntegrationsResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListWebhookIntegrationsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListWebhookIntegrationsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListWebhookIntegrationsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListWebhookIntegrationsResponse400
    | ListWebhookIntegrationsResponse401
    | ListWebhookIntegrationsResponse403
    | ListWebhookIntegrationsResponse404
    | ListWebhookIntegrationsResponse423
    | ListWebhookIntegrationsResponse429
    | ListWebhookIntegrationsResponse500
    | ListWebhookIntegrationsResponse503
    | WebhookIntegrationList
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
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    ListWebhookIntegrationsResponse400
    | ListWebhookIntegrationsResponse401
    | ListWebhookIntegrationsResponse403
    | ListWebhookIntegrationsResponse404
    | ListWebhookIntegrationsResponse423
    | ListWebhookIntegrationsResponse429
    | ListWebhookIntegrationsResponse500
    | ListWebhookIntegrationsResponse503
    | WebhookIntegrationList
]:
    """List webhook integrations

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookIntegrationsResponse400 | ListWebhookIntegrationsResponse401 | ListWebhookIntegrationsResponse403 | ListWebhookIntegrationsResponse404 | ListWebhookIntegrationsResponse423 | ListWebhookIntegrationsResponse429 | ListWebhookIntegrationsResponse500 | ListWebhookIntegrationsResponse503 | WebhookIntegrationList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        starting_after=starting_after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    ListWebhookIntegrationsResponse400
    | ListWebhookIntegrationsResponse401
    | ListWebhookIntegrationsResponse403
    | ListWebhookIntegrationsResponse404
    | ListWebhookIntegrationsResponse423
    | ListWebhookIntegrationsResponse429
    | ListWebhookIntegrationsResponse500
    | ListWebhookIntegrationsResponse503
    | WebhookIntegrationList
    | None
):
    """List webhook integrations

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookIntegrationsResponse400 | ListWebhookIntegrationsResponse401 | ListWebhookIntegrationsResponse403 | ListWebhookIntegrationsResponse404 | ListWebhookIntegrationsResponse423 | ListWebhookIntegrationsResponse429 | ListWebhookIntegrationsResponse500 | ListWebhookIntegrationsResponse503 | WebhookIntegrationList
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        starting_after=starting_after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    ListWebhookIntegrationsResponse400
    | ListWebhookIntegrationsResponse401
    | ListWebhookIntegrationsResponse403
    | ListWebhookIntegrationsResponse404
    | ListWebhookIntegrationsResponse423
    | ListWebhookIntegrationsResponse429
    | ListWebhookIntegrationsResponse500
    | ListWebhookIntegrationsResponse503
    | WebhookIntegrationList
]:
    """List webhook integrations

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookIntegrationsResponse400 | ListWebhookIntegrationsResponse401 | ListWebhookIntegrationsResponse403 | ListWebhookIntegrationsResponse404 | ListWebhookIntegrationsResponse423 | ListWebhookIntegrationsResponse429 | ListWebhookIntegrationsResponse500 | ListWebhookIntegrationsResponse503 | WebhookIntegrationList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        starting_after=starting_after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    ListWebhookIntegrationsResponse400
    | ListWebhookIntegrationsResponse401
    | ListWebhookIntegrationsResponse403
    | ListWebhookIntegrationsResponse404
    | ListWebhookIntegrationsResponse423
    | ListWebhookIntegrationsResponse429
    | ListWebhookIntegrationsResponse500
    | ListWebhookIntegrationsResponse503
    | WebhookIntegrationList
    | None
):
    """List webhook integrations

     This endpoint requires the following permission(s):
    <code>project_configuration:integrations:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookIntegrationsResponse400 | ListWebhookIntegrationsResponse401 | ListWebhookIntegrationsResponse403 | ListWebhookIntegrationsResponse404 | ListWebhookIntegrationsResponse423 | ListWebhookIntegrationsResponse429 | ListWebhookIntegrationsResponse500 | ListWebhookIntegrationsResponse503 | WebhookIntegrationList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            starting_after=starting_after,
            limit=limit,
        )
    ).parsed
