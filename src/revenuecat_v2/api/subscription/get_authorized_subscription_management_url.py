from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authenticated_management_url import AuthenticatedManagementUrl
from ...models.get_authorized_subscription_management_url_response_400 import (
    GetAuthorizedSubscriptionManagementUrlResponse400,
)
from ...models.get_authorized_subscription_management_url_response_401 import (
    GetAuthorizedSubscriptionManagementUrlResponse401,
)
from ...models.get_authorized_subscription_management_url_response_403 import (
    GetAuthorizedSubscriptionManagementUrlResponse403,
)
from ...models.get_authorized_subscription_management_url_response_404 import (
    GetAuthorizedSubscriptionManagementUrlResponse404,
)
from ...models.get_authorized_subscription_management_url_response_423 import (
    GetAuthorizedSubscriptionManagementUrlResponse423,
)
from ...models.get_authorized_subscription_management_url_response_429 import (
    GetAuthorizedSubscriptionManagementUrlResponse429,
)
from ...models.get_authorized_subscription_management_url_response_500 import (
    GetAuthorizedSubscriptionManagementUrlResponse500,
)
from ...models.get_authorized_subscription_management_url_response_503 import (
    GetAuthorizedSubscriptionManagementUrlResponse503,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/subscriptions/{subscription_id}/authenticated_management_url".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AuthenticatedManagementUrl
    | GetAuthorizedSubscriptionManagementUrlResponse400
    | GetAuthorizedSubscriptionManagementUrlResponse401
    | GetAuthorizedSubscriptionManagementUrlResponse403
    | GetAuthorizedSubscriptionManagementUrlResponse404
    | GetAuthorizedSubscriptionManagementUrlResponse423
    | GetAuthorizedSubscriptionManagementUrlResponse429
    | GetAuthorizedSubscriptionManagementUrlResponse500
    | GetAuthorizedSubscriptionManagementUrlResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AuthenticatedManagementUrl.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAuthorizedSubscriptionManagementUrlResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetAuthorizedSubscriptionManagementUrlResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetAuthorizedSubscriptionManagementUrlResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAuthorizedSubscriptionManagementUrlResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetAuthorizedSubscriptionManagementUrlResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetAuthorizedSubscriptionManagementUrlResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetAuthorizedSubscriptionManagementUrlResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetAuthorizedSubscriptionManagementUrlResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AuthenticatedManagementUrl
    | GetAuthorizedSubscriptionManagementUrlResponse400
    | GetAuthorizedSubscriptionManagementUrlResponse401
    | GetAuthorizedSubscriptionManagementUrlResponse403
    | GetAuthorizedSubscriptionManagementUrlResponse404
    | GetAuthorizedSubscriptionManagementUrlResponse423
    | GetAuthorizedSubscriptionManagementUrlResponse429
    | GetAuthorizedSubscriptionManagementUrlResponse500
    | GetAuthorizedSubscriptionManagementUrlResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AuthenticatedManagementUrl
    | GetAuthorizedSubscriptionManagementUrlResponse400
    | GetAuthorizedSubscriptionManagementUrlResponse401
    | GetAuthorizedSubscriptionManagementUrlResponse403
    | GetAuthorizedSubscriptionManagementUrlResponse404
    | GetAuthorizedSubscriptionManagementUrlResponse423
    | GetAuthorizedSubscriptionManagementUrlResponse429
    | GetAuthorizedSubscriptionManagementUrlResponse500
    | GetAuthorizedSubscriptionManagementUrlResponse503
]:
    """Get an authenticated Web Billing customer portal URL

     Get a secure, single-use URL that allows customers to access their Web Billing customer portal.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthenticatedManagementUrl | GetAuthorizedSubscriptionManagementUrlResponse400 | GetAuthorizedSubscriptionManagementUrlResponse401 | GetAuthorizedSubscriptionManagementUrlResponse403 | GetAuthorizedSubscriptionManagementUrlResponse404 | GetAuthorizedSubscriptionManagementUrlResponse423 | GetAuthorizedSubscriptionManagementUrlResponse429 | GetAuthorizedSubscriptionManagementUrlResponse500 | GetAuthorizedSubscriptionManagementUrlResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AuthenticatedManagementUrl
    | GetAuthorizedSubscriptionManagementUrlResponse400
    | GetAuthorizedSubscriptionManagementUrlResponse401
    | GetAuthorizedSubscriptionManagementUrlResponse403
    | GetAuthorizedSubscriptionManagementUrlResponse404
    | GetAuthorizedSubscriptionManagementUrlResponse423
    | GetAuthorizedSubscriptionManagementUrlResponse429
    | GetAuthorizedSubscriptionManagementUrlResponse500
    | GetAuthorizedSubscriptionManagementUrlResponse503
    | None
):
    """Get an authenticated Web Billing customer portal URL

     Get a secure, single-use URL that allows customers to access their Web Billing customer portal.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthenticatedManagementUrl | GetAuthorizedSubscriptionManagementUrlResponse400 | GetAuthorizedSubscriptionManagementUrlResponse401 | GetAuthorizedSubscriptionManagementUrlResponse403 | GetAuthorizedSubscriptionManagementUrlResponse404 | GetAuthorizedSubscriptionManagementUrlResponse423 | GetAuthorizedSubscriptionManagementUrlResponse429 | GetAuthorizedSubscriptionManagementUrlResponse500 | GetAuthorizedSubscriptionManagementUrlResponse503
    """

    return sync_detailed(
        project_id=project_id,
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AuthenticatedManagementUrl
    | GetAuthorizedSubscriptionManagementUrlResponse400
    | GetAuthorizedSubscriptionManagementUrlResponse401
    | GetAuthorizedSubscriptionManagementUrlResponse403
    | GetAuthorizedSubscriptionManagementUrlResponse404
    | GetAuthorizedSubscriptionManagementUrlResponse423
    | GetAuthorizedSubscriptionManagementUrlResponse429
    | GetAuthorizedSubscriptionManagementUrlResponse500
    | GetAuthorizedSubscriptionManagementUrlResponse503
]:
    """Get an authenticated Web Billing customer portal URL

     Get a secure, single-use URL that allows customers to access their Web Billing customer portal.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthenticatedManagementUrl | GetAuthorizedSubscriptionManagementUrlResponse400 | GetAuthorizedSubscriptionManagementUrlResponse401 | GetAuthorizedSubscriptionManagementUrlResponse403 | GetAuthorizedSubscriptionManagementUrlResponse404 | GetAuthorizedSubscriptionManagementUrlResponse423 | GetAuthorizedSubscriptionManagementUrlResponse429 | GetAuthorizedSubscriptionManagementUrlResponse500 | GetAuthorizedSubscriptionManagementUrlResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AuthenticatedManagementUrl
    | GetAuthorizedSubscriptionManagementUrlResponse400
    | GetAuthorizedSubscriptionManagementUrlResponse401
    | GetAuthorizedSubscriptionManagementUrlResponse403
    | GetAuthorizedSubscriptionManagementUrlResponse404
    | GetAuthorizedSubscriptionManagementUrlResponse423
    | GetAuthorizedSubscriptionManagementUrlResponse429
    | GetAuthorizedSubscriptionManagementUrlResponse500
    | GetAuthorizedSubscriptionManagementUrlResponse503
    | None
):
    """Get an authenticated Web Billing customer portal URL

     Get a secure, single-use URL that allows customers to access their Web Billing customer portal.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthenticatedManagementUrl | GetAuthorizedSubscriptionManagementUrlResponse400 | GetAuthorizedSubscriptionManagementUrlResponse401 | GetAuthorizedSubscriptionManagementUrlResponse403 | GetAuthorizedSubscriptionManagementUrlResponse404 | GetAuthorizedSubscriptionManagementUrlResponse423 | GetAuthorizedSubscriptionManagementUrlResponse429 | GetAuthorizedSubscriptionManagementUrlResponse500 | GetAuthorizedSubscriptionManagementUrlResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
