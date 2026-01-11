from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_play_store_subscription_transactions_response_400 import (
    GetPlayStoreSubscriptionTransactionsResponse400,
)
from ...models.get_play_store_subscription_transactions_response_401 import (
    GetPlayStoreSubscriptionTransactionsResponse401,
)
from ...models.get_play_store_subscription_transactions_response_403 import (
    GetPlayStoreSubscriptionTransactionsResponse403,
)
from ...models.get_play_store_subscription_transactions_response_404 import (
    GetPlayStoreSubscriptionTransactionsResponse404,
)
from ...models.get_play_store_subscription_transactions_response_423 import (
    GetPlayStoreSubscriptionTransactionsResponse423,
)
from ...models.get_play_store_subscription_transactions_response_429 import (
    GetPlayStoreSubscriptionTransactionsResponse429,
)
from ...models.get_play_store_subscription_transactions_response_500 import (
    GetPlayStoreSubscriptionTransactionsResponse500,
)
from ...models.get_play_store_subscription_transactions_response_503 import (
    GetPlayStoreSubscriptionTransactionsResponse503,
)
from ...models.subscription_transaction_list import SubscriptionTransactionList
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/subscriptions/{subscription_id}/transactions".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetPlayStoreSubscriptionTransactionsResponse400
    | GetPlayStoreSubscriptionTransactionsResponse401
    | GetPlayStoreSubscriptionTransactionsResponse403
    | GetPlayStoreSubscriptionTransactionsResponse404
    | GetPlayStoreSubscriptionTransactionsResponse423
    | GetPlayStoreSubscriptionTransactionsResponse429
    | GetPlayStoreSubscriptionTransactionsResponse500
    | GetPlayStoreSubscriptionTransactionsResponse503
    | SubscriptionTransactionList
    | None
):
    if response.status_code == 200:
        response_200 = SubscriptionTransactionList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetPlayStoreSubscriptionTransactionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetPlayStoreSubscriptionTransactionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetPlayStoreSubscriptionTransactionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetPlayStoreSubscriptionTransactionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetPlayStoreSubscriptionTransactionsResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetPlayStoreSubscriptionTransactionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetPlayStoreSubscriptionTransactionsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetPlayStoreSubscriptionTransactionsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetPlayStoreSubscriptionTransactionsResponse400
    | GetPlayStoreSubscriptionTransactionsResponse401
    | GetPlayStoreSubscriptionTransactionsResponse403
    | GetPlayStoreSubscriptionTransactionsResponse404
    | GetPlayStoreSubscriptionTransactionsResponse423
    | GetPlayStoreSubscriptionTransactionsResponse429
    | GetPlayStoreSubscriptionTransactionsResponse500
    | GetPlayStoreSubscriptionTransactionsResponse503
    | SubscriptionTransactionList
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
    GetPlayStoreSubscriptionTransactionsResponse400
    | GetPlayStoreSubscriptionTransactionsResponse401
    | GetPlayStoreSubscriptionTransactionsResponse403
    | GetPlayStoreSubscriptionTransactionsResponse404
    | GetPlayStoreSubscriptionTransactionsResponse423
    | GetPlayStoreSubscriptionTransactionsResponse429
    | GetPlayStoreSubscriptionTransactionsResponse500
    | GetPlayStoreSubscriptionTransactionsResponse503
    | SubscriptionTransactionList
]:
    """Get a Play Store subscription's transactions

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
        Response[GetPlayStoreSubscriptionTransactionsResponse400 | GetPlayStoreSubscriptionTransactionsResponse401 | GetPlayStoreSubscriptionTransactionsResponse403 | GetPlayStoreSubscriptionTransactionsResponse404 | GetPlayStoreSubscriptionTransactionsResponse423 | GetPlayStoreSubscriptionTransactionsResponse429 | GetPlayStoreSubscriptionTransactionsResponse500 | GetPlayStoreSubscriptionTransactionsResponse503 | SubscriptionTransactionList]
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
    GetPlayStoreSubscriptionTransactionsResponse400
    | GetPlayStoreSubscriptionTransactionsResponse401
    | GetPlayStoreSubscriptionTransactionsResponse403
    | GetPlayStoreSubscriptionTransactionsResponse404
    | GetPlayStoreSubscriptionTransactionsResponse423
    | GetPlayStoreSubscriptionTransactionsResponse429
    | GetPlayStoreSubscriptionTransactionsResponse500
    | GetPlayStoreSubscriptionTransactionsResponse503
    | SubscriptionTransactionList
    | None
):
    """Get a Play Store subscription's transactions

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
        GetPlayStoreSubscriptionTransactionsResponse400 | GetPlayStoreSubscriptionTransactionsResponse401 | GetPlayStoreSubscriptionTransactionsResponse403 | GetPlayStoreSubscriptionTransactionsResponse404 | GetPlayStoreSubscriptionTransactionsResponse423 | GetPlayStoreSubscriptionTransactionsResponse429 | GetPlayStoreSubscriptionTransactionsResponse500 | GetPlayStoreSubscriptionTransactionsResponse503 | SubscriptionTransactionList
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
    GetPlayStoreSubscriptionTransactionsResponse400
    | GetPlayStoreSubscriptionTransactionsResponse401
    | GetPlayStoreSubscriptionTransactionsResponse403
    | GetPlayStoreSubscriptionTransactionsResponse404
    | GetPlayStoreSubscriptionTransactionsResponse423
    | GetPlayStoreSubscriptionTransactionsResponse429
    | GetPlayStoreSubscriptionTransactionsResponse500
    | GetPlayStoreSubscriptionTransactionsResponse503
    | SubscriptionTransactionList
]:
    """Get a Play Store subscription's transactions

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
        Response[GetPlayStoreSubscriptionTransactionsResponse400 | GetPlayStoreSubscriptionTransactionsResponse401 | GetPlayStoreSubscriptionTransactionsResponse403 | GetPlayStoreSubscriptionTransactionsResponse404 | GetPlayStoreSubscriptionTransactionsResponse423 | GetPlayStoreSubscriptionTransactionsResponse429 | GetPlayStoreSubscriptionTransactionsResponse500 | GetPlayStoreSubscriptionTransactionsResponse503 | SubscriptionTransactionList]
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
    GetPlayStoreSubscriptionTransactionsResponse400
    | GetPlayStoreSubscriptionTransactionsResponse401
    | GetPlayStoreSubscriptionTransactionsResponse403
    | GetPlayStoreSubscriptionTransactionsResponse404
    | GetPlayStoreSubscriptionTransactionsResponse423
    | GetPlayStoreSubscriptionTransactionsResponse429
    | GetPlayStoreSubscriptionTransactionsResponse500
    | GetPlayStoreSubscriptionTransactionsResponse503
    | SubscriptionTransactionList
    | None
):
    """Get a Play Store subscription's transactions

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
        GetPlayStoreSubscriptionTransactionsResponse400 | GetPlayStoreSubscriptionTransactionsResponse401 | GetPlayStoreSubscriptionTransactionsResponse403 | GetPlayStoreSubscriptionTransactionsResponse404 | GetPlayStoreSubscriptionTransactionsResponse423 | GetPlayStoreSubscriptionTransactionsResponse429 | GetPlayStoreSubscriptionTransactionsResponse500 | GetPlayStoreSubscriptionTransactionsResponse503 | SubscriptionTransactionList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
