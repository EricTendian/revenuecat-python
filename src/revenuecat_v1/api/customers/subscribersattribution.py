from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.subscribersattribution_body import SubscribersattributionBody
from ...models.subscribersattribution_response_200 import SubscribersattributionResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_user_id: str,
    *,
    body: SubscribersattributionBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subscribers/{app_user_id}/attribution".format(
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
) -> SubscribersattributionResponse200 | None:
    if response.status_code == 200:
        response_200 = SubscribersattributionResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SubscribersattributionResponse200]:
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
    body: SubscribersattributionBody | Unset = UNSET,
) -> Response[SubscribersattributionResponse200]:
    """Add Customer Attribution Data

     Attaches attribution data to a subscriber from specific supported networks.

    Args:
        app_user_id (str):
        body (SubscribersattributionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscribersattributionResponse200]
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
    body: SubscribersattributionBody | Unset = UNSET,
) -> SubscribersattributionResponse200 | None:
    """Add Customer Attribution Data

     Attaches attribution data to a subscriber from specific supported networks.

    Args:
        app_user_id (str):
        body (SubscribersattributionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscribersattributionResponse200
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
    body: SubscribersattributionBody | Unset = UNSET,
) -> Response[SubscribersattributionResponse200]:
    """Add Customer Attribution Data

     Attaches attribution data to a subscriber from specific supported networks.

    Args:
        app_user_id (str):
        body (SubscribersattributionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscribersattributionResponse200]
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
    body: SubscribersattributionBody | Unset = UNSET,
) -> SubscribersattributionResponse200 | None:
    """Add Customer Attribution Data

     Attaches attribution data to a subscriber from specific supported networks.

    Args:
        app_user_id (str):
        body (SubscribersattributionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscribersattributionResponse200
    """

    return (
        await asyncio_detailed(
            app_user_id=app_user_id,
            client=client,
            body=body,
        )
    ).parsed
