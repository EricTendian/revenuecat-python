from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.defer_a_google_subscription_body import DeferAGoogleSubscriptionBody
from ...models.subscriber import Subscriber
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_user_id: str,
    product_identifier: str,
    *,
    body: DeferAGoogleSubscriptionBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subscribers/{app_user_id}/subscriptions/{product_identifier}/defer".format(
            app_user_id=quote(str(app_user_id), safe=""),
            product_identifier=quote(str(product_identifier), safe=""),
        ),
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
    app_user_id: str,
    product_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeferAGoogleSubscriptionBody | Unset = UNSET,
) -> Response[Subscriber]:
    """Google Play: Defer a Subscription

     Defers the purchase of a Google Subscription to a later date.

    Args:
        app_user_id (str):
        product_identifier (str):
        body (DeferAGoogleSubscriptionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscriber]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        product_identifier=product_identifier,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_user_id: str,
    product_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeferAGoogleSubscriptionBody | Unset = UNSET,
) -> Subscriber | None:
    """Google Play: Defer a Subscription

     Defers the purchase of a Google Subscription to a later date.

    Args:
        app_user_id (str):
        product_identifier (str):
        body (DeferAGoogleSubscriptionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscriber
    """

    return sync_detailed(
        app_user_id=app_user_id,
        product_identifier=product_identifier,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_user_id: str,
    product_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeferAGoogleSubscriptionBody | Unset = UNSET,
) -> Response[Subscriber]:
    """Google Play: Defer a Subscription

     Defers the purchase of a Google Subscription to a later date.

    Args:
        app_user_id (str):
        product_identifier (str):
        body (DeferAGoogleSubscriptionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscriber]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        product_identifier=product_identifier,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_user_id: str,
    product_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeferAGoogleSubscriptionBody | Unset = UNSET,
) -> Subscriber | None:
    """Google Play: Defer a Subscription

     Defers the purchase of a Google Subscription to a later date.

    Args:
        app_user_id (str):
        product_identifier (str):
        body (DeferAGoogleSubscriptionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscriber
    """

    return (
        await asyncio_detailed(
            app_user_id=app_user_id,
            product_identifier=product_identifier,
            client=client,
            body=body,
        )
    ).parsed
