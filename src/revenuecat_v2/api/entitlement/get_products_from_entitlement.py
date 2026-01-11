from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_products_from_entitlement_response_400 import GetProductsFromEntitlementResponse400
from ...models.get_products_from_entitlement_response_401 import GetProductsFromEntitlementResponse401
from ...models.get_products_from_entitlement_response_403 import GetProductsFromEntitlementResponse403
from ...models.get_products_from_entitlement_response_404 import GetProductsFromEntitlementResponse404
from ...models.get_products_from_entitlement_response_423 import GetProductsFromEntitlementResponse423
from ...models.get_products_from_entitlement_response_429 import GetProductsFromEntitlementResponse429
from ...models.get_products_from_entitlement_response_500 import GetProductsFromEntitlementResponse500
from ...models.get_products_from_entitlement_response_503 import GetProductsFromEntitlementResponse503
from ...models.products_from_entitlement_list import ProductsFromEntitlementList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    entitlement_id: str,
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
        "url": "/projects/{project_id}/entitlements/{entitlement_id}/products".format(
            project_id=quote(str(project_id), safe=""),
            entitlement_id=quote(str(entitlement_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetProductsFromEntitlementResponse400
    | GetProductsFromEntitlementResponse401
    | GetProductsFromEntitlementResponse403
    | GetProductsFromEntitlementResponse404
    | GetProductsFromEntitlementResponse423
    | GetProductsFromEntitlementResponse429
    | GetProductsFromEntitlementResponse500
    | GetProductsFromEntitlementResponse503
    | ProductsFromEntitlementList
    | None
):
    if response.status_code == 200:
        response_200 = ProductsFromEntitlementList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetProductsFromEntitlementResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetProductsFromEntitlementResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetProductsFromEntitlementResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetProductsFromEntitlementResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetProductsFromEntitlementResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetProductsFromEntitlementResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetProductsFromEntitlementResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetProductsFromEntitlementResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetProductsFromEntitlementResponse400
    | GetProductsFromEntitlementResponse401
    | GetProductsFromEntitlementResponse403
    | GetProductsFromEntitlementResponse404
    | GetProductsFromEntitlementResponse423
    | GetProductsFromEntitlementResponse429
    | GetProductsFromEntitlementResponse500
    | GetProductsFromEntitlementResponse503
    | ProductsFromEntitlementList
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    GetProductsFromEntitlementResponse400
    | GetProductsFromEntitlementResponse401
    | GetProductsFromEntitlementResponse403
    | GetProductsFromEntitlementResponse404
    | GetProductsFromEntitlementResponse423
    | GetProductsFromEntitlementResponse429
    | GetProductsFromEntitlementResponse500
    | GetProductsFromEntitlementResponse503
    | ProductsFromEntitlementList
]:
    """Get a list of products attached to a given entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductsFromEntitlementResponse400 | GetProductsFromEntitlementResponse401 | GetProductsFromEntitlementResponse403 | GetProductsFromEntitlementResponse404 | GetProductsFromEntitlementResponse423 | GetProductsFromEntitlementResponse429 | GetProductsFromEntitlementResponse500 | GetProductsFromEntitlementResponse503 | ProductsFromEntitlementList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        entitlement_id=entitlement_id,
        starting_after=starting_after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    GetProductsFromEntitlementResponse400
    | GetProductsFromEntitlementResponse401
    | GetProductsFromEntitlementResponse403
    | GetProductsFromEntitlementResponse404
    | GetProductsFromEntitlementResponse423
    | GetProductsFromEntitlementResponse429
    | GetProductsFromEntitlementResponse500
    | GetProductsFromEntitlementResponse503
    | ProductsFromEntitlementList
    | None
):
    """Get a list of products attached to a given entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductsFromEntitlementResponse400 | GetProductsFromEntitlementResponse401 | GetProductsFromEntitlementResponse403 | GetProductsFromEntitlementResponse404 | GetProductsFromEntitlementResponse423 | GetProductsFromEntitlementResponse429 | GetProductsFromEntitlementResponse500 | GetProductsFromEntitlementResponse503 | ProductsFromEntitlementList
    """

    return sync_detailed(
        project_id=project_id,
        entitlement_id=entitlement_id,
        client=client,
        starting_after=starting_after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    GetProductsFromEntitlementResponse400
    | GetProductsFromEntitlementResponse401
    | GetProductsFromEntitlementResponse403
    | GetProductsFromEntitlementResponse404
    | GetProductsFromEntitlementResponse423
    | GetProductsFromEntitlementResponse429
    | GetProductsFromEntitlementResponse500
    | GetProductsFromEntitlementResponse503
    | ProductsFromEntitlementList
]:
    """Get a list of products attached to a given entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductsFromEntitlementResponse400 | GetProductsFromEntitlementResponse401 | GetProductsFromEntitlementResponse403 | GetProductsFromEntitlementResponse404 | GetProductsFromEntitlementResponse423 | GetProductsFromEntitlementResponse429 | GetProductsFromEntitlementResponse500 | GetProductsFromEntitlementResponse503 | ProductsFromEntitlementList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        entitlement_id=entitlement_id,
        starting_after=starting_after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    entitlement_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    GetProductsFromEntitlementResponse400
    | GetProductsFromEntitlementResponse401
    | GetProductsFromEntitlementResponse403
    | GetProductsFromEntitlementResponse404
    | GetProductsFromEntitlementResponse423
    | GetProductsFromEntitlementResponse429
    | GetProductsFromEntitlementResponse500
    | GetProductsFromEntitlementResponse503
    | ProductsFromEntitlementList
    | None
):
    """Get a list of products attached to a given entitlement

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        entitlement_id (str):  Example: entla1b2c3d4e5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductsFromEntitlementResponse400 | GetProductsFromEntitlementResponse401 | GetProductsFromEntitlementResponse403 | GetProductsFromEntitlementResponse404 | GetProductsFromEntitlementResponse423 | GetProductsFromEntitlementResponse429 | GetProductsFromEntitlementResponse500 | GetProductsFromEntitlementResponse503 | ProductsFromEntitlementList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            entitlement_id=entitlement_id,
            client=client,
            starting_after=starting_after,
            limit=limit,
        )
    ).parsed
