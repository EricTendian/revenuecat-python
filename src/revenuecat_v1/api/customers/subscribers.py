from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.subscriber import Subscriber
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_user_id: str,
    *,
    x_platform: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_platform, Unset):
        headers["X-Platform"] = x_platform

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subscribers/{app_user_id}".format(
            app_user_id=quote(str(app_user_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Subscriber | None:
    if response.status_code == 200:
        response_200 = Subscriber.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Subscriber.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Subscriber]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_platform: str | Unset = UNSET,
) -> Response[Error | Subscriber]:
    """Get or Create Customer

     Gets the latest [Customer Info](#tag/customer_info_model) for the customer with the given App User
    ID, or creates a new customer if it doesn't exist.

    Args:
        app_user_id (str):
        x_platform (str | Unset):  Example: ios.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Subscriber]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        x_platform=x_platform,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_platform: str | Unset = UNSET,
) -> Error | Subscriber | None:
    """Get or Create Customer

     Gets the latest [Customer Info](#tag/customer_info_model) for the customer with the given App User
    ID, or creates a new customer if it doesn't exist.

    Args:
        app_user_id (str):
        x_platform (str | Unset):  Example: ios.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Subscriber
    """

    return sync_detailed(
        app_user_id=app_user_id,
        client=client,
        x_platform=x_platform,
    ).parsed


async def asyncio_detailed(
    app_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_platform: str | Unset = UNSET,
) -> Response[Error | Subscriber]:
    """Get or Create Customer

     Gets the latest [Customer Info](#tag/customer_info_model) for the customer with the given App User
    ID, or creates a new customer if it doesn't exist.

    Args:
        app_user_id (str):
        x_platform (str | Unset):  Example: ios.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Subscriber]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        x_platform=x_platform,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_platform: str | Unset = UNSET,
) -> Error | Subscriber | None:
    """Get or Create Customer

     Gets the latest [Customer Info](#tag/customer_info_model) for the customer with the given App User
    ID, or creates a new customer if it doesn't exist.

    Args:
        app_user_id (str):
        x_platform (str | Unset):  Example: ios.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Subscriber
    """

    return (
        await asyncio_detailed(
            app_user_id=app_user_id,
            client=client,
            x_platform=x_platform,
        )
    ).parsed
