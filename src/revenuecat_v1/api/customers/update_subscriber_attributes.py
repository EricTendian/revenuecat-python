from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.subscriber import Subscriber
from ...models.update_subscriber_attributes_body import UpdateSubscriberAttributesBody
from ...models.update_subscriber_attributes_response_400 import UpdateSubscriberAttributesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_user_id: str,
    *,
    body: UpdateSubscriberAttributesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subscribers/{app_user_id}/attributes".format(
            app_user_id=quote(str(app_user_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Subscriber | UpdateSubscriberAttributesResponse400 | None:
    if response.status_code == 200:
        response_200 = Subscriber.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateSubscriberAttributesResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Subscriber | UpdateSubscriberAttributesResponse400]:
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
    body: UpdateSubscriberAttributesBody | Unset = UNSET,
) -> Response[Subscriber | UpdateSubscriberAttributesResponse400]:
    """Update Customer Attributes

     Updates attributes for a customer.

    Args:
        app_user_id (str):
        body (UpdateSubscriberAttributesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscriber | UpdateSubscriberAttributesResponse400]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSubscriberAttributesBody | Unset = UNSET,
) -> Subscriber | UpdateSubscriberAttributesResponse400 | None:
    """Update Customer Attributes

     Updates attributes for a customer.

    Args:
        app_user_id (str):
        body (UpdateSubscriberAttributesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscriber | UpdateSubscriberAttributesResponse400
    """

    return sync_detailed(
        app_user_id=app_user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSubscriberAttributesBody | Unset = UNSET,
) -> Response[Subscriber | UpdateSubscriberAttributesResponse400]:
    """Update Customer Attributes

     Updates attributes for a customer.

    Args:
        app_user_id (str):
        body (UpdateSubscriberAttributesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscriber | UpdateSubscriberAttributesResponse400]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSubscriberAttributesBody | Unset = UNSET,
) -> Subscriber | UpdateSubscriberAttributesResponse400 | None:
    """Update Customer Attributes

     Updates attributes for a customer.

    Args:
        app_user_id (str):
        body (UpdateSubscriberAttributesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscriber | UpdateSubscriberAttributesResponse400
    """

    return (
        await asyncio_detailed(
            app_user_id=app_user_id,
            client=client,
            body=body,
        )
    ).parsed
