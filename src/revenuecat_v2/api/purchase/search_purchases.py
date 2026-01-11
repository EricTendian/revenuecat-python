from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.purchase_list import PurchaseList
from ...models.search_purchases_response_400 import SearchPurchasesResponse400
from ...models.search_purchases_response_401 import SearchPurchasesResponse401
from ...models.search_purchases_response_403 import SearchPurchasesResponse403
from ...models.search_purchases_response_404 import SearchPurchasesResponse404
from ...models.search_purchases_response_423 import SearchPurchasesResponse423
from ...models.search_purchases_response_429 import SearchPurchasesResponse429
from ...models.search_purchases_response_500 import SearchPurchasesResponse500
from ...models.search_purchases_response_503 import SearchPurchasesResponse503
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    store_purchase_identifier: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["store_purchase_identifier"] = store_purchase_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/purchases".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PurchaseList
    | SearchPurchasesResponse400
    | SearchPurchasesResponse401
    | SearchPurchasesResponse403
    | SearchPurchasesResponse404
    | SearchPurchasesResponse423
    | SearchPurchasesResponse429
    | SearchPurchasesResponse500
    | SearchPurchasesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PurchaseList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SearchPurchasesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SearchPurchasesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SearchPurchasesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SearchPurchasesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = SearchPurchasesResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = SearchPurchasesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SearchPurchasesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SearchPurchasesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PurchaseList
    | SearchPurchasesResponse400
    | SearchPurchasesResponse401
    | SearchPurchasesResponse403
    | SearchPurchasesResponse404
    | SearchPurchasesResponse423
    | SearchPurchasesResponse429
    | SearchPurchasesResponse500
    | SearchPurchasesResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    store_purchase_identifier: str,
) -> Response[
    PurchaseList
    | SearchPurchasesResponse400
    | SearchPurchasesResponse401
    | SearchPurchasesResponse403
    | SearchPurchasesResponse404
    | SearchPurchasesResponse423
    | SearchPurchasesResponse429
    | SearchPurchasesResponse500
    | SearchPurchasesResponse503
]:
    """Search one-time purchases by store purchase identifier

     Search for a one-time purchases by any of its associated `store_purchase_identifier` values.

    For example, this may include the `transactionId` of any transaction in an Apple App Store purchase,
    or any order ID from a Google Play Store purchase.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        store_purchase_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseList | SearchPurchasesResponse400 | SearchPurchasesResponse401 | SearchPurchasesResponse403 | SearchPurchasesResponse404 | SearchPurchasesResponse423 | SearchPurchasesResponse429 | SearchPurchasesResponse500 | SearchPurchasesResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        store_purchase_identifier=store_purchase_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    store_purchase_identifier: str,
) -> (
    PurchaseList
    | SearchPurchasesResponse400
    | SearchPurchasesResponse401
    | SearchPurchasesResponse403
    | SearchPurchasesResponse404
    | SearchPurchasesResponse423
    | SearchPurchasesResponse429
    | SearchPurchasesResponse500
    | SearchPurchasesResponse503
    | None
):
    """Search one-time purchases by store purchase identifier

     Search for a one-time purchases by any of its associated `store_purchase_identifier` values.

    For example, this may include the `transactionId` of any transaction in an Apple App Store purchase,
    or any order ID from a Google Play Store purchase.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        store_purchase_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseList | SearchPurchasesResponse400 | SearchPurchasesResponse401 | SearchPurchasesResponse403 | SearchPurchasesResponse404 | SearchPurchasesResponse423 | SearchPurchasesResponse429 | SearchPurchasesResponse500 | SearchPurchasesResponse503
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        store_purchase_identifier=store_purchase_identifier,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    store_purchase_identifier: str,
) -> Response[
    PurchaseList
    | SearchPurchasesResponse400
    | SearchPurchasesResponse401
    | SearchPurchasesResponse403
    | SearchPurchasesResponse404
    | SearchPurchasesResponse423
    | SearchPurchasesResponse429
    | SearchPurchasesResponse500
    | SearchPurchasesResponse503
]:
    """Search one-time purchases by store purchase identifier

     Search for a one-time purchases by any of its associated `store_purchase_identifier` values.

    For example, this may include the `transactionId` of any transaction in an Apple App Store purchase,
    or any order ID from a Google Play Store purchase.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        store_purchase_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseList | SearchPurchasesResponse400 | SearchPurchasesResponse401 | SearchPurchasesResponse403 | SearchPurchasesResponse404 | SearchPurchasesResponse423 | SearchPurchasesResponse429 | SearchPurchasesResponse500 | SearchPurchasesResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        store_purchase_identifier=store_purchase_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    store_purchase_identifier: str,
) -> (
    PurchaseList
    | SearchPurchasesResponse400
    | SearchPurchasesResponse401
    | SearchPurchasesResponse403
    | SearchPurchasesResponse404
    | SearchPurchasesResponse423
    | SearchPurchasesResponse429
    | SearchPurchasesResponse500
    | SearchPurchasesResponse503
    | None
):
    """Search one-time purchases by store purchase identifier

     Search for a one-time purchases by any of its associated `store_purchase_identifier` values.

    For example, this may include the `transactionId` of any transaction in an Apple App Store purchase,
    or any order ID from a Google Play Store purchase.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        store_purchase_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseList | SearchPurchasesResponse400 | SearchPurchasesResponse401 | SearchPurchasesResponse403 | SearchPurchasesResponse404 | SearchPurchasesResponse423 | SearchPurchasesResponse429 | SearchPurchasesResponse500 | SearchPurchasesResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            store_purchase_identifier=store_purchase_identifier,
        )
    ).parsed
