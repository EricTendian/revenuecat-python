from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_subscriber_response_200 import DeleteSubscriberResponse200
from ...types import Response


def _get_kwargs(
    app_user_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/subscribers/{app_user_id}".format(
            app_user_id=quote(str(app_user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteSubscriberResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteSubscriberResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteSubscriberResponse200]:
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
) -> Response[DeleteSubscriberResponse200]:
    """Delete Customer

     Permanently deletes a customer.

    Args:
        app_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSubscriberResponse200]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteSubscriberResponse200 | None:
    """Delete Customer

     Permanently deletes a customer.

    Args:
        app_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSubscriberResponse200
    """

    return sync_detailed(
        app_user_id=app_user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteSubscriberResponse200]:
    """Delete Customer

     Permanently deletes a customer.

    Args:
        app_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSubscriberResponse200]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteSubscriberResponse200 | None:
    """Delete Customer

     Permanently deletes a customer.

    Args:
        app_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSubscriberResponse200
    """

    return (
        await asyncio_detailed(
            app_user_id=app_user_id,
            client=client,
        )
    ).parsed
