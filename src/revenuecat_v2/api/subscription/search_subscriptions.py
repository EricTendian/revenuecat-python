from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_subscriptions_response_400 import SearchSubscriptionsResponse400
from ...models.search_subscriptions_response_401 import SearchSubscriptionsResponse401
from ...models.search_subscriptions_response_403 import SearchSubscriptionsResponse403
from ...models.search_subscriptions_response_404 import SearchSubscriptionsResponse404
from ...models.search_subscriptions_response_423 import SearchSubscriptionsResponse423
from ...models.search_subscriptions_response_429 import SearchSubscriptionsResponse429
from ...models.search_subscriptions_response_500 import SearchSubscriptionsResponse500
from ...models.search_subscriptions_response_503 import SearchSubscriptionsResponse503
from ...models.subscription_list import SubscriptionList
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    store_subscription_identifier: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["store_subscription_identifier"] = store_subscription_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/subscriptions".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SearchSubscriptionsResponse400
    | SearchSubscriptionsResponse401
    | SearchSubscriptionsResponse403
    | SearchSubscriptionsResponse404
    | SearchSubscriptionsResponse423
    | SearchSubscriptionsResponse429
    | SearchSubscriptionsResponse500
    | SearchSubscriptionsResponse503
    | SubscriptionList
    | None
):
    if response.status_code == 200:
        response_200 = SubscriptionList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SearchSubscriptionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SearchSubscriptionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SearchSubscriptionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SearchSubscriptionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = SearchSubscriptionsResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = SearchSubscriptionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SearchSubscriptionsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SearchSubscriptionsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SearchSubscriptionsResponse400
    | SearchSubscriptionsResponse401
    | SearchSubscriptionsResponse403
    | SearchSubscriptionsResponse404
    | SearchSubscriptionsResponse423
    | SearchSubscriptionsResponse429
    | SearchSubscriptionsResponse500
    | SearchSubscriptionsResponse503
    | SubscriptionList
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
    store_subscription_identifier: str,
) -> Response[
    SearchSubscriptionsResponse400
    | SearchSubscriptionsResponse401
    | SearchSubscriptionsResponse403
    | SearchSubscriptionsResponse404
    | SearchSubscriptionsResponse423
    | SearchSubscriptionsResponse429
    | SearchSubscriptionsResponse500
    | SearchSubscriptionsResponse503
    | SubscriptionList
]:
    """Search subscriptions by store subscription identifier

     Search for a subscription by any of its associated `store_subscription_identifier` values, whether
    from a past or current subscription period.

    For example, this may include the `transactionId` of any transaction in an Apple App Store
    subscription, or any order ID from a Google Play Store subscription.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        store_subscription_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSubscriptionsResponse400 | SearchSubscriptionsResponse401 | SearchSubscriptionsResponse403 | SearchSubscriptionsResponse404 | SearchSubscriptionsResponse423 | SearchSubscriptionsResponse429 | SearchSubscriptionsResponse500 | SearchSubscriptionsResponse503 | SubscriptionList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        store_subscription_identifier=store_subscription_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    store_subscription_identifier: str,
) -> (
    SearchSubscriptionsResponse400
    | SearchSubscriptionsResponse401
    | SearchSubscriptionsResponse403
    | SearchSubscriptionsResponse404
    | SearchSubscriptionsResponse423
    | SearchSubscriptionsResponse429
    | SearchSubscriptionsResponse500
    | SearchSubscriptionsResponse503
    | SubscriptionList
    | None
):
    """Search subscriptions by store subscription identifier

     Search for a subscription by any of its associated `store_subscription_identifier` values, whether
    from a past or current subscription period.

    For example, this may include the `transactionId` of any transaction in an Apple App Store
    subscription, or any order ID from a Google Play Store subscription.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        store_subscription_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSubscriptionsResponse400 | SearchSubscriptionsResponse401 | SearchSubscriptionsResponse403 | SearchSubscriptionsResponse404 | SearchSubscriptionsResponse423 | SearchSubscriptionsResponse429 | SearchSubscriptionsResponse500 | SearchSubscriptionsResponse503 | SubscriptionList
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        store_subscription_identifier=store_subscription_identifier,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    store_subscription_identifier: str,
) -> Response[
    SearchSubscriptionsResponse400
    | SearchSubscriptionsResponse401
    | SearchSubscriptionsResponse403
    | SearchSubscriptionsResponse404
    | SearchSubscriptionsResponse423
    | SearchSubscriptionsResponse429
    | SearchSubscriptionsResponse500
    | SearchSubscriptionsResponse503
    | SubscriptionList
]:
    """Search subscriptions by store subscription identifier

     Search for a subscription by any of its associated `store_subscription_identifier` values, whether
    from a past or current subscription period.

    For example, this may include the `transactionId` of any transaction in an Apple App Store
    subscription, or any order ID from a Google Play Store subscription.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        store_subscription_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSubscriptionsResponse400 | SearchSubscriptionsResponse401 | SearchSubscriptionsResponse403 | SearchSubscriptionsResponse404 | SearchSubscriptionsResponse423 | SearchSubscriptionsResponse429 | SearchSubscriptionsResponse500 | SearchSubscriptionsResponse503 | SubscriptionList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        store_subscription_identifier=store_subscription_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    store_subscription_identifier: str,
) -> (
    SearchSubscriptionsResponse400
    | SearchSubscriptionsResponse401
    | SearchSubscriptionsResponse403
    | SearchSubscriptionsResponse404
    | SearchSubscriptionsResponse423
    | SearchSubscriptionsResponse429
    | SearchSubscriptionsResponse500
    | SearchSubscriptionsResponse503
    | SubscriptionList
    | None
):
    """Search subscriptions by store subscription identifier

     Search for a subscription by any of its associated `store_subscription_identifier` values, whether
    from a past or current subscription period.

    For example, this may include the `transactionId` of any transaction in an Apple App Store
    subscription, or any order ID from a Google Play Store subscription.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        store_subscription_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSubscriptionsResponse400 | SearchSubscriptionsResponse401 | SearchSubscriptionsResponse403 | SearchSubscriptionsResponse404 | SearchSubscriptionsResponse423 | SearchSubscriptionsResponse429 | SearchSubscriptionsResponse500 | SearchSubscriptionsResponse503 | SubscriptionList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            store_subscription_identifier=store_subscription_identifier,
        )
    ).parsed
