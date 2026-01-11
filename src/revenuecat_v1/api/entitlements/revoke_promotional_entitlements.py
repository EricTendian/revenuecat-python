from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.subscriber import Subscriber
from ...types import Response


def _get_kwargs(
    app_user_id: str,
    entitlement_identifier: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subscribers/{app_user_id}/entitlements/{entitlement_identifier}/revoke_promotionals".format(
            app_user_id=quote(str(app_user_id), safe=""),
            entitlement_identifier=quote(str(entitlement_identifier), safe=""),
        ),
    }

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
    entitlement_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Subscriber]:
    """Revoke Granted Entitlements

     Revokes all granted entitlements for a given entitlement identifier and App User ID.

    Args:
        app_user_id (str):
        entitlement_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscriber]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        entitlement_identifier=entitlement_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_user_id: str,
    entitlement_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Subscriber | None:
    """Revoke Granted Entitlements

     Revokes all granted entitlements for a given entitlement identifier and App User ID.

    Args:
        app_user_id (str):
        entitlement_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscriber
    """

    return sync_detailed(
        app_user_id=app_user_id,
        entitlement_identifier=entitlement_identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_user_id: str,
    entitlement_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Subscriber]:
    """Revoke Granted Entitlements

     Revokes all granted entitlements for a given entitlement identifier and App User ID.

    Args:
        app_user_id (str):
        entitlement_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscriber]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        entitlement_identifier=entitlement_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_user_id: str,
    entitlement_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Subscriber | None:
    """Revoke Granted Entitlements

     Revokes all granted entitlements for a given entitlement identifier and App User ID.

    Args:
        app_user_id (str):
        entitlement_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscriber
    """

    return (
        await asyncio_detailed(
            app_user_id=app_user_id,
            entitlement_identifier=entitlement_identifier,
            client=client,
        )
    ).parsed
