from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.refund_play_store_subscription_transaction_response_400 import (
    RefundPlayStoreSubscriptionTransactionResponse400,
)
from ...models.refund_play_store_subscription_transaction_response_401 import (
    RefundPlayStoreSubscriptionTransactionResponse401,
)
from ...models.refund_play_store_subscription_transaction_response_403 import (
    RefundPlayStoreSubscriptionTransactionResponse403,
)
from ...models.refund_play_store_subscription_transaction_response_404 import (
    RefundPlayStoreSubscriptionTransactionResponse404,
)
from ...models.refund_play_store_subscription_transaction_response_409 import (
    RefundPlayStoreSubscriptionTransactionResponse409,
)
from ...models.refund_play_store_subscription_transaction_response_422 import (
    RefundPlayStoreSubscriptionTransactionResponse422,
)
from ...models.refund_play_store_subscription_transaction_response_423 import (
    RefundPlayStoreSubscriptionTransactionResponse423,
)
from ...models.refund_play_store_subscription_transaction_response_429 import (
    RefundPlayStoreSubscriptionTransactionResponse429,
)
from ...models.refund_play_store_subscription_transaction_response_500 import (
    RefundPlayStoreSubscriptionTransactionResponse500,
)
from ...models.refund_play_store_subscription_transaction_response_503 import (
    RefundPlayStoreSubscriptionTransactionResponse503,
)
from ...models.subscription_transaction import SubscriptionTransaction
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
    transaction_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/subscriptions/{subscription_id}/transactions/{transaction_id}/actions/refund".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
            transaction_id=quote(str(transaction_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RefundPlayStoreSubscriptionTransactionResponse400
    | RefundPlayStoreSubscriptionTransactionResponse401
    | RefundPlayStoreSubscriptionTransactionResponse403
    | RefundPlayStoreSubscriptionTransactionResponse404
    | RefundPlayStoreSubscriptionTransactionResponse409
    | RefundPlayStoreSubscriptionTransactionResponse422
    | RefundPlayStoreSubscriptionTransactionResponse423
    | RefundPlayStoreSubscriptionTransactionResponse429
    | RefundPlayStoreSubscriptionTransactionResponse500
    | RefundPlayStoreSubscriptionTransactionResponse503
    | SubscriptionTransaction
    | None
):
    if response.status_code == 200:
        response_200 = SubscriptionTransaction.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RefundPlayStoreSubscriptionTransactionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RefundPlayStoreSubscriptionTransactionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RefundPlayStoreSubscriptionTransactionResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RefundPlayStoreSubscriptionTransactionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = RefundPlayStoreSubscriptionTransactionResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = RefundPlayStoreSubscriptionTransactionResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = RefundPlayStoreSubscriptionTransactionResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = RefundPlayStoreSubscriptionTransactionResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RefundPlayStoreSubscriptionTransactionResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RefundPlayStoreSubscriptionTransactionResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RefundPlayStoreSubscriptionTransactionResponse400
    | RefundPlayStoreSubscriptionTransactionResponse401
    | RefundPlayStoreSubscriptionTransactionResponse403
    | RefundPlayStoreSubscriptionTransactionResponse404
    | RefundPlayStoreSubscriptionTransactionResponse409
    | RefundPlayStoreSubscriptionTransactionResponse422
    | RefundPlayStoreSubscriptionTransactionResponse423
    | RefundPlayStoreSubscriptionTransactionResponse429
    | RefundPlayStoreSubscriptionTransactionResponse500
    | RefundPlayStoreSubscriptionTransactionResponse503
    | SubscriptionTransaction
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
    transaction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    RefundPlayStoreSubscriptionTransactionResponse400
    | RefundPlayStoreSubscriptionTransactionResponse401
    | RefundPlayStoreSubscriptionTransactionResponse403
    | RefundPlayStoreSubscriptionTransactionResponse404
    | RefundPlayStoreSubscriptionTransactionResponse409
    | RefundPlayStoreSubscriptionTransactionResponse422
    | RefundPlayStoreSubscriptionTransactionResponse423
    | RefundPlayStoreSubscriptionTransactionResponse429
    | RefundPlayStoreSubscriptionTransactionResponse500
    | RefundPlayStoreSubscriptionTransactionResponse503
    | SubscriptionTransaction
]:
    """Refund a Play Store subscription's transaction

     Refund a Play Store subscription's transaction. This endpoint does not cancel the subscription or
    revoke access to it.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.
        transaction_id (str):  Example: GPA.000-000-000-000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefundPlayStoreSubscriptionTransactionResponse400 | RefundPlayStoreSubscriptionTransactionResponse401 | RefundPlayStoreSubscriptionTransactionResponse403 | RefundPlayStoreSubscriptionTransactionResponse404 | RefundPlayStoreSubscriptionTransactionResponse409 | RefundPlayStoreSubscriptionTransactionResponse422 | RefundPlayStoreSubscriptionTransactionResponse423 | RefundPlayStoreSubscriptionTransactionResponse429 | RefundPlayStoreSubscriptionTransactionResponse500 | RefundPlayStoreSubscriptionTransactionResponse503 | SubscriptionTransaction]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
        transaction_id=transaction_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    subscription_id: str,
    transaction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    RefundPlayStoreSubscriptionTransactionResponse400
    | RefundPlayStoreSubscriptionTransactionResponse401
    | RefundPlayStoreSubscriptionTransactionResponse403
    | RefundPlayStoreSubscriptionTransactionResponse404
    | RefundPlayStoreSubscriptionTransactionResponse409
    | RefundPlayStoreSubscriptionTransactionResponse422
    | RefundPlayStoreSubscriptionTransactionResponse423
    | RefundPlayStoreSubscriptionTransactionResponse429
    | RefundPlayStoreSubscriptionTransactionResponse500
    | RefundPlayStoreSubscriptionTransactionResponse503
    | SubscriptionTransaction
    | None
):
    """Refund a Play Store subscription's transaction

     Refund a Play Store subscription's transaction. This endpoint does not cancel the subscription or
    revoke access to it.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.
        transaction_id (str):  Example: GPA.000-000-000-000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefundPlayStoreSubscriptionTransactionResponse400 | RefundPlayStoreSubscriptionTransactionResponse401 | RefundPlayStoreSubscriptionTransactionResponse403 | RefundPlayStoreSubscriptionTransactionResponse404 | RefundPlayStoreSubscriptionTransactionResponse409 | RefundPlayStoreSubscriptionTransactionResponse422 | RefundPlayStoreSubscriptionTransactionResponse423 | RefundPlayStoreSubscriptionTransactionResponse429 | RefundPlayStoreSubscriptionTransactionResponse500 | RefundPlayStoreSubscriptionTransactionResponse503 | SubscriptionTransaction
    """

    return sync_detailed(
        project_id=project_id,
        subscription_id=subscription_id,
        transaction_id=transaction_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    subscription_id: str,
    transaction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    RefundPlayStoreSubscriptionTransactionResponse400
    | RefundPlayStoreSubscriptionTransactionResponse401
    | RefundPlayStoreSubscriptionTransactionResponse403
    | RefundPlayStoreSubscriptionTransactionResponse404
    | RefundPlayStoreSubscriptionTransactionResponse409
    | RefundPlayStoreSubscriptionTransactionResponse422
    | RefundPlayStoreSubscriptionTransactionResponse423
    | RefundPlayStoreSubscriptionTransactionResponse429
    | RefundPlayStoreSubscriptionTransactionResponse500
    | RefundPlayStoreSubscriptionTransactionResponse503
    | SubscriptionTransaction
]:
    """Refund a Play Store subscription's transaction

     Refund a Play Store subscription's transaction. This endpoint does not cancel the subscription or
    revoke access to it.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.
        transaction_id (str):  Example: GPA.000-000-000-000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefundPlayStoreSubscriptionTransactionResponse400 | RefundPlayStoreSubscriptionTransactionResponse401 | RefundPlayStoreSubscriptionTransactionResponse403 | RefundPlayStoreSubscriptionTransactionResponse404 | RefundPlayStoreSubscriptionTransactionResponse409 | RefundPlayStoreSubscriptionTransactionResponse422 | RefundPlayStoreSubscriptionTransactionResponse423 | RefundPlayStoreSubscriptionTransactionResponse429 | RefundPlayStoreSubscriptionTransactionResponse500 | RefundPlayStoreSubscriptionTransactionResponse503 | SubscriptionTransaction]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
        transaction_id=transaction_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    subscription_id: str,
    transaction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    RefundPlayStoreSubscriptionTransactionResponse400
    | RefundPlayStoreSubscriptionTransactionResponse401
    | RefundPlayStoreSubscriptionTransactionResponse403
    | RefundPlayStoreSubscriptionTransactionResponse404
    | RefundPlayStoreSubscriptionTransactionResponse409
    | RefundPlayStoreSubscriptionTransactionResponse422
    | RefundPlayStoreSubscriptionTransactionResponse423
    | RefundPlayStoreSubscriptionTransactionResponse429
    | RefundPlayStoreSubscriptionTransactionResponse500
    | RefundPlayStoreSubscriptionTransactionResponse503
    | SubscriptionTransaction
    | None
):
    """Refund a Play Store subscription's transaction

     Refund a Play Store subscription's transaction. This endpoint does not cancel the subscription or
    revoke access to it.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.
        transaction_id (str):  Example: GPA.000-000-000-000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefundPlayStoreSubscriptionTransactionResponse400 | RefundPlayStoreSubscriptionTransactionResponse401 | RefundPlayStoreSubscriptionTransactionResponse403 | RefundPlayStoreSubscriptionTransactionResponse404 | RefundPlayStoreSubscriptionTransactionResponse409 | RefundPlayStoreSubscriptionTransactionResponse422 | RefundPlayStoreSubscriptionTransactionResponse423 | RefundPlayStoreSubscriptionTransactionResponse429 | RefundPlayStoreSubscriptionTransactionResponse500 | RefundPlayStoreSubscriptionTransactionResponse503 | SubscriptionTransaction
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            transaction_id=transaction_id,
            client=client,
        )
    ).parsed
