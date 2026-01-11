from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entitlement_list import EntitlementList
from ...models.list_purchase_entitlements_response_400 import ListPurchaseEntitlementsResponse400
from ...models.list_purchase_entitlements_response_401 import ListPurchaseEntitlementsResponse401
from ...models.list_purchase_entitlements_response_403 import ListPurchaseEntitlementsResponse403
from ...models.list_purchase_entitlements_response_404 import ListPurchaseEntitlementsResponse404
from ...models.list_purchase_entitlements_response_423 import ListPurchaseEntitlementsResponse423
from ...models.list_purchase_entitlements_response_429 import ListPurchaseEntitlementsResponse429
from ...models.list_purchase_entitlements_response_500 import ListPurchaseEntitlementsResponse500
from ...models.list_purchase_entitlements_response_503 import ListPurchaseEntitlementsResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    purchase_id: str,
    *,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["starting_after"] = starting_after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/purchases/{purchase_id}/entitlements".format(
            project_id=quote(str(project_id), safe=""),
            purchase_id=quote(str(purchase_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EntitlementList
    | ListPurchaseEntitlementsResponse400
    | ListPurchaseEntitlementsResponse401
    | ListPurchaseEntitlementsResponse403
    | ListPurchaseEntitlementsResponse404
    | ListPurchaseEntitlementsResponse423
    | ListPurchaseEntitlementsResponse429
    | ListPurchaseEntitlementsResponse500
    | ListPurchaseEntitlementsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = EntitlementList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListPurchaseEntitlementsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListPurchaseEntitlementsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListPurchaseEntitlementsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListPurchaseEntitlementsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListPurchaseEntitlementsResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListPurchaseEntitlementsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListPurchaseEntitlementsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListPurchaseEntitlementsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EntitlementList
    | ListPurchaseEntitlementsResponse400
    | ListPurchaseEntitlementsResponse401
    | ListPurchaseEntitlementsResponse403
    | ListPurchaseEntitlementsResponse404
    | ListPurchaseEntitlementsResponse423
    | ListPurchaseEntitlementsResponse429
    | ListPurchaseEntitlementsResponse500
    | ListPurchaseEntitlementsResponse503
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
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    EntitlementList
    | ListPurchaseEntitlementsResponse400
    | ListPurchaseEntitlementsResponse401
    | ListPurchaseEntitlementsResponse403
    | ListPurchaseEntitlementsResponse404
    | ListPurchaseEntitlementsResponse423
    | ListPurchaseEntitlementsResponse429
    | ListPurchaseEntitlementsResponse500
    | ListPurchaseEntitlementsResponse503
]:
    """Get a list of entitlements associated with a purchase

     Lists all Entitlements granted by a Purchase.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntitlementList | ListPurchaseEntitlementsResponse400 | ListPurchaseEntitlementsResponse401 | ListPurchaseEntitlementsResponse403 | ListPurchaseEntitlementsResponse404 | ListPurchaseEntitlementsResponse423 | ListPurchaseEntitlementsResponse429 | ListPurchaseEntitlementsResponse500 | ListPurchaseEntitlementsResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        purchase_id=purchase_id,
        starting_after=starting_after,
        limit=limit,
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
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    EntitlementList
    | ListPurchaseEntitlementsResponse400
    | ListPurchaseEntitlementsResponse401
    | ListPurchaseEntitlementsResponse403
    | ListPurchaseEntitlementsResponse404
    | ListPurchaseEntitlementsResponse423
    | ListPurchaseEntitlementsResponse429
    | ListPurchaseEntitlementsResponse500
    | ListPurchaseEntitlementsResponse503
    | None
):
    """Get a list of entitlements associated with a purchase

     Lists all Entitlements granted by a Purchase.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntitlementList | ListPurchaseEntitlementsResponse400 | ListPurchaseEntitlementsResponse401 | ListPurchaseEntitlementsResponse403 | ListPurchaseEntitlementsResponse404 | ListPurchaseEntitlementsResponse423 | ListPurchaseEntitlementsResponse429 | ListPurchaseEntitlementsResponse500 | ListPurchaseEntitlementsResponse503
    """

    return sync_detailed(
        project_id=project_id,
        purchase_id=purchase_id,
        client=client,
        starting_after=starting_after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    purchase_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    EntitlementList
    | ListPurchaseEntitlementsResponse400
    | ListPurchaseEntitlementsResponse401
    | ListPurchaseEntitlementsResponse403
    | ListPurchaseEntitlementsResponse404
    | ListPurchaseEntitlementsResponse423
    | ListPurchaseEntitlementsResponse429
    | ListPurchaseEntitlementsResponse500
    | ListPurchaseEntitlementsResponse503
]:
    """Get a list of entitlements associated with a purchase

     Lists all Entitlements granted by a Purchase.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntitlementList | ListPurchaseEntitlementsResponse400 | ListPurchaseEntitlementsResponse401 | ListPurchaseEntitlementsResponse403 | ListPurchaseEntitlementsResponse404 | ListPurchaseEntitlementsResponse423 | ListPurchaseEntitlementsResponse429 | ListPurchaseEntitlementsResponse500 | ListPurchaseEntitlementsResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        purchase_id=purchase_id,
        starting_after=starting_after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    purchase_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    EntitlementList
    | ListPurchaseEntitlementsResponse400
    | ListPurchaseEntitlementsResponse401
    | ListPurchaseEntitlementsResponse403
    | ListPurchaseEntitlementsResponse404
    | ListPurchaseEntitlementsResponse423
    | ListPurchaseEntitlementsResponse429
    | ListPurchaseEntitlementsResponse500
    | ListPurchaseEntitlementsResponse503
    | None
):
    """Get a list of entitlements associated with a purchase

     Lists all Entitlements granted by a Purchase.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntitlementList | ListPurchaseEntitlementsResponse400 | ListPurchaseEntitlementsResponse401 | ListPurchaseEntitlementsResponse403 | ListPurchaseEntitlementsResponse404 | ListPurchaseEntitlementsResponse423 | ListPurchaseEntitlementsResponse429 | ListPurchaseEntitlementsResponse500 | ListPurchaseEntitlementsResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            purchase_id=purchase_id,
            client=client,
            starting_after=starting_after,
            limit=limit,
        )
    ).parsed
