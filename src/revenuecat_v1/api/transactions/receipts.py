from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.receipts_body import ReceiptsBody
from ...models.subscriber import Subscriber
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ReceiptsBody | Unset = UNSET,
    x_platform: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Platform"] = x_platform

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/receipts",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Subscriber | None:
    if response.status_code == 200:
        response_200 = Subscriber.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Subscriber]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReceiptsBody | Unset = UNSET,
    x_platform: str,
) -> Response[Subscriber]:
    """Create a Purchase

     Records a purchase for a Customer from iOS, Android, Stripe, Roku and Paddle will create a Customer
    if they don't already exist.

    Args:
        x_platform (str):  Example: ios.
        body (ReceiptsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscriber]
    """

    kwargs = _get_kwargs(
        body=body,
        x_platform=x_platform,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ReceiptsBody | Unset = UNSET,
    x_platform: str,
) -> Subscriber | None:
    """Create a Purchase

     Records a purchase for a Customer from iOS, Android, Stripe, Roku and Paddle will create a Customer
    if they don't already exist.

    Args:
        x_platform (str):  Example: ios.
        body (ReceiptsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscriber
    """

    return sync_detailed(
        client=client,
        body=body,
        x_platform=x_platform,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReceiptsBody | Unset = UNSET,
    x_platform: str,
) -> Response[Subscriber]:
    """Create a Purchase

     Records a purchase for a Customer from iOS, Android, Stripe, Roku and Paddle will create a Customer
    if they don't already exist.

    Args:
        x_platform (str):  Example: ios.
        body (ReceiptsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscriber]
    """

    kwargs = _get_kwargs(
        body=body,
        x_platform=x_platform,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReceiptsBody | Unset = UNSET,
    x_platform: str,
) -> Subscriber | None:
    """Create a Purchase

     Records a purchase for a Customer from iOS, Android, Stripe, Roku and Paddle will create a Customer
    if they don't already exist.

    Args:
        x_platform (str):  Example: ios.
        body (ReceiptsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscriber
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_platform=x_platform,
        )
    ).parsed
