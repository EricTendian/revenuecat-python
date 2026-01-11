from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.refund_subscription_response_400 import RefundSubscriptionResponse400
from ...models.refund_subscription_response_401 import RefundSubscriptionResponse401
from ...models.refund_subscription_response_403 import RefundSubscriptionResponse403
from ...models.refund_subscription_response_404 import RefundSubscriptionResponse404
from ...models.refund_subscription_response_409 import RefundSubscriptionResponse409
from ...models.refund_subscription_response_422 import RefundSubscriptionResponse422
from ...models.refund_subscription_response_423 import RefundSubscriptionResponse423
from ...models.refund_subscription_response_429 import RefundSubscriptionResponse429
from ...models.refund_subscription_response_500 import RefundSubscriptionResponse500
from ...models.refund_subscription_response_503 import RefundSubscriptionResponse503
from ...models.subscription import Subscription
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/subscriptions/{subscription_id}/actions/refund".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RefundSubscriptionResponse400
    | RefundSubscriptionResponse401
    | RefundSubscriptionResponse403
    | RefundSubscriptionResponse404
    | RefundSubscriptionResponse409
    | RefundSubscriptionResponse422
    | RefundSubscriptionResponse423
    | RefundSubscriptionResponse429
    | RefundSubscriptionResponse500
    | RefundSubscriptionResponse503
    | Subscription
    | None
):
    if response.status_code == 200:
        response_200 = Subscription.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RefundSubscriptionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RefundSubscriptionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RefundSubscriptionResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RefundSubscriptionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = RefundSubscriptionResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = RefundSubscriptionResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = RefundSubscriptionResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = RefundSubscriptionResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RefundSubscriptionResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RefundSubscriptionResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RefundSubscriptionResponse400
    | RefundSubscriptionResponse401
    | RefundSubscriptionResponse403
    | RefundSubscriptionResponse404
    | RefundSubscriptionResponse409
    | RefundSubscriptionResponse422
    | RefundSubscriptionResponse423
    | RefundSubscriptionResponse429
    | RefundSubscriptionResponse500
    | RefundSubscriptionResponse503
    | Subscription
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
    RefundSubscriptionResponse400
    | RefundSubscriptionResponse401
    | RefundSubscriptionResponse403
    | RefundSubscriptionResponse404
    | RefundSubscriptionResponse409
    | RefundSubscriptionResponse422
    | RefundSubscriptionResponse423
    | RefundSubscriptionResponse429
    | RefundSubscriptionResponse500
    | RefundSubscriptionResponse503
    | Subscription
]:
    """Refund an active Web Billing subscription

     Cancel a Web Billing subscription by refunding the most recent payment. The customer will
    immediately lose access to the associated entitlements.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefundSubscriptionResponse400 | RefundSubscriptionResponse401 | RefundSubscriptionResponse403 | RefundSubscriptionResponse404 | RefundSubscriptionResponse409 | RefundSubscriptionResponse422 | RefundSubscriptionResponse423 | RefundSubscriptionResponse429 | RefundSubscriptionResponse500 | RefundSubscriptionResponse503 | Subscription]
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
    RefundSubscriptionResponse400
    | RefundSubscriptionResponse401
    | RefundSubscriptionResponse403
    | RefundSubscriptionResponse404
    | RefundSubscriptionResponse409
    | RefundSubscriptionResponse422
    | RefundSubscriptionResponse423
    | RefundSubscriptionResponse429
    | RefundSubscriptionResponse500
    | RefundSubscriptionResponse503
    | Subscription
    | None
):
    """Refund an active Web Billing subscription

     Cancel a Web Billing subscription by refunding the most recent payment. The customer will
    immediately lose access to the associated entitlements.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefundSubscriptionResponse400 | RefundSubscriptionResponse401 | RefundSubscriptionResponse403 | RefundSubscriptionResponse404 | RefundSubscriptionResponse409 | RefundSubscriptionResponse422 | RefundSubscriptionResponse423 | RefundSubscriptionResponse429 | RefundSubscriptionResponse500 | RefundSubscriptionResponse503 | Subscription
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
    RefundSubscriptionResponse400
    | RefundSubscriptionResponse401
    | RefundSubscriptionResponse403
    | RefundSubscriptionResponse404
    | RefundSubscriptionResponse409
    | RefundSubscriptionResponse422
    | RefundSubscriptionResponse423
    | RefundSubscriptionResponse429
    | RefundSubscriptionResponse500
    | RefundSubscriptionResponse503
    | Subscription
]:
    """Refund an active Web Billing subscription

     Cancel a Web Billing subscription by refunding the most recent payment. The customer will
    immediately lose access to the associated entitlements.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefundSubscriptionResponse400 | RefundSubscriptionResponse401 | RefundSubscriptionResponse403 | RefundSubscriptionResponse404 | RefundSubscriptionResponse409 | RefundSubscriptionResponse422 | RefundSubscriptionResponse423 | RefundSubscriptionResponse429 | RefundSubscriptionResponse500 | RefundSubscriptionResponse503 | Subscription]
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
    RefundSubscriptionResponse400
    | RefundSubscriptionResponse401
    | RefundSubscriptionResponse403
    | RefundSubscriptionResponse404
    | RefundSubscriptionResponse409
    | RefundSubscriptionResponse422
    | RefundSubscriptionResponse423
    | RefundSubscriptionResponse429
    | RefundSubscriptionResponse500
    | RefundSubscriptionResponse503
    | Subscription
    | None
):
    """Refund an active Web Billing subscription

     Cancel a Web Billing subscription by refunding the most recent payment. The customer will
    immediately lose access to the associated entitlements.
     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        subscription_id (str):  Example: sub1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefundSubscriptionResponse400 | RefundSubscriptionResponse401 | RefundSubscriptionResponse403 | RefundSubscriptionResponse404 | RefundSubscriptionResponse409 | RefundSubscriptionResponse422 | RefundSubscriptionResponse423 | RefundSubscriptionResponse429 | RefundSubscriptionResponse500 | RefundSubscriptionResponse503 | Subscription
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
