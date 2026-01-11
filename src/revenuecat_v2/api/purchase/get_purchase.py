from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_purchase_response_400 import GetPurchaseResponse400
from ...models.get_purchase_response_401 import GetPurchaseResponse401
from ...models.get_purchase_response_403 import GetPurchaseResponse403
from ...models.get_purchase_response_404 import GetPurchaseResponse404
from ...models.get_purchase_response_423 import GetPurchaseResponse423
from ...models.get_purchase_response_429 import GetPurchaseResponse429
from ...models.get_purchase_response_500 import GetPurchaseResponse500
from ...models.get_purchase_response_503 import GetPurchaseResponse503
from ...models.purchase import Purchase
from ...types import Response


def _get_kwargs(
    project_id: str,
    purchase_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/purchases/{purchase_id}".format(
            project_id=quote(str(project_id), safe=""),
            purchase_id=quote(str(purchase_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetPurchaseResponse400
    | GetPurchaseResponse401
    | GetPurchaseResponse403
    | GetPurchaseResponse404
    | GetPurchaseResponse423
    | GetPurchaseResponse429
    | GetPurchaseResponse500
    | GetPurchaseResponse503
    | Purchase
    | None
):
    if response.status_code == 200:
        response_200 = Purchase.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetPurchaseResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetPurchaseResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetPurchaseResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetPurchaseResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetPurchaseResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetPurchaseResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetPurchaseResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetPurchaseResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetPurchaseResponse400
    | GetPurchaseResponse401
    | GetPurchaseResponse403
    | GetPurchaseResponse404
    | GetPurchaseResponse423
    | GetPurchaseResponse429
    | GetPurchaseResponse500
    | GetPurchaseResponse503
    | Purchase
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    purchase_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetPurchaseResponse400
    | GetPurchaseResponse401
    | GetPurchaseResponse403
    | GetPurchaseResponse404
    | GetPurchaseResponse423
    | GetPurchaseResponse429
    | GetPurchaseResponse500
    | GetPurchaseResponse503
    | Purchase
]:
    """Get a purchase

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseResponse400 | GetPurchaseResponse401 | GetPurchaseResponse403 | GetPurchaseResponse404 | GetPurchaseResponse423 | GetPurchaseResponse429 | GetPurchaseResponse500 | GetPurchaseResponse503 | Purchase]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        purchase_id=purchase_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    purchase_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetPurchaseResponse400
    | GetPurchaseResponse401
    | GetPurchaseResponse403
    | GetPurchaseResponse404
    | GetPurchaseResponse423
    | GetPurchaseResponse429
    | GetPurchaseResponse500
    | GetPurchaseResponse503
    | Purchase
    | None
):
    """Get a purchase

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPurchaseResponse400 | GetPurchaseResponse401 | GetPurchaseResponse403 | GetPurchaseResponse404 | GetPurchaseResponse423 | GetPurchaseResponse429 | GetPurchaseResponse500 | GetPurchaseResponse503 | Purchase
    """

    return sync_detailed(
        project_id=project_id,
        purchase_id=purchase_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    purchase_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetPurchaseResponse400
    | GetPurchaseResponse401
    | GetPurchaseResponse403
    | GetPurchaseResponse404
    | GetPurchaseResponse423
    | GetPurchaseResponse429
    | GetPurchaseResponse500
    | GetPurchaseResponse503
    | Purchase
]:
    """Get a purchase

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseResponse400 | GetPurchaseResponse401 | GetPurchaseResponse403 | GetPurchaseResponse404 | GetPurchaseResponse423 | GetPurchaseResponse429 | GetPurchaseResponse500 | GetPurchaseResponse503 | Purchase]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        purchase_id=purchase_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    purchase_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetPurchaseResponse400
    | GetPurchaseResponse401
    | GetPurchaseResponse403
    | GetPurchaseResponse404
    | GetPurchaseResponse423
    | GetPurchaseResponse429
    | GetPurchaseResponse500
    | GetPurchaseResponse503
    | Purchase
    | None
):
    """Get a purchase

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPurchaseResponse400 | GetPurchaseResponse401 | GetPurchaseResponse403 | GetPurchaseResponse404 | GetPurchaseResponse423 | GetPurchaseResponse429 | GetPurchaseResponse500 | GetPurchaseResponse503 | Purchase
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            purchase_id=purchase_id,
            client=client,
        )
    ).parsed
