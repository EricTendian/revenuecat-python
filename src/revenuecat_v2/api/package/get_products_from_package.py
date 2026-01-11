from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_products_from_package_response_400 import GetProductsFromPackageResponse400
from ...models.get_products_from_package_response_401 import GetProductsFromPackageResponse401
from ...models.get_products_from_package_response_403 import GetProductsFromPackageResponse403
from ...models.get_products_from_package_response_404 import GetProductsFromPackageResponse404
from ...models.get_products_from_package_response_423 import GetProductsFromPackageResponse423
from ...models.get_products_from_package_response_429 import GetProductsFromPackageResponse429
from ...models.get_products_from_package_response_500 import GetProductsFromPackageResponse500
from ...models.get_products_from_package_response_503 import GetProductsFromPackageResponse503
from ...models.products_from_package_list import ProductsFromPackageList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    package_id: str,
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
        "url": "/projects/{project_id}/packages/{package_id}/products".format(
            project_id=quote(str(project_id), safe=""),
            package_id=quote(str(package_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetProductsFromPackageResponse400
    | GetProductsFromPackageResponse401
    | GetProductsFromPackageResponse403
    | GetProductsFromPackageResponse404
    | GetProductsFromPackageResponse423
    | GetProductsFromPackageResponse429
    | GetProductsFromPackageResponse500
    | GetProductsFromPackageResponse503
    | ProductsFromPackageList
    | None
):
    if response.status_code == 200:
        response_200 = ProductsFromPackageList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetProductsFromPackageResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetProductsFromPackageResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetProductsFromPackageResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetProductsFromPackageResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetProductsFromPackageResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetProductsFromPackageResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetProductsFromPackageResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetProductsFromPackageResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetProductsFromPackageResponse400
    | GetProductsFromPackageResponse401
    | GetProductsFromPackageResponse403
    | GetProductsFromPackageResponse404
    | GetProductsFromPackageResponse423
    | GetProductsFromPackageResponse429
    | GetProductsFromPackageResponse500
    | GetProductsFromPackageResponse503
    | ProductsFromPackageList
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    GetProductsFromPackageResponse400
    | GetProductsFromPackageResponse401
    | GetProductsFromPackageResponse403
    | GetProductsFromPackageResponse404
    | GetProductsFromPackageResponse423
    | GetProductsFromPackageResponse429
    | GetProductsFromPackageResponse500
    | GetProductsFromPackageResponse503
    | ProductsFromPackageList
]:
    """Get a list of products attached to a given package of an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductsFromPackageResponse400 | GetProductsFromPackageResponse401 | GetProductsFromPackageResponse403 | GetProductsFromPackageResponse404 | GetProductsFromPackageResponse423 | GetProductsFromPackageResponse429 | GetProductsFromPackageResponse500 | GetProductsFromPackageResponse503 | ProductsFromPackageList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        package_id=package_id,
        starting_after=starting_after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    GetProductsFromPackageResponse400
    | GetProductsFromPackageResponse401
    | GetProductsFromPackageResponse403
    | GetProductsFromPackageResponse404
    | GetProductsFromPackageResponse423
    | GetProductsFromPackageResponse429
    | GetProductsFromPackageResponse500
    | GetProductsFromPackageResponse503
    | ProductsFromPackageList
    | None
):
    """Get a list of products attached to a given package of an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductsFromPackageResponse400 | GetProductsFromPackageResponse401 | GetProductsFromPackageResponse403 | GetProductsFromPackageResponse404 | GetProductsFromPackageResponse423 | GetProductsFromPackageResponse429 | GetProductsFromPackageResponse500 | GetProductsFromPackageResponse503 | ProductsFromPackageList
    """

    return sync_detailed(
        project_id=project_id,
        package_id=package_id,
        client=client,
        starting_after=starting_after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    GetProductsFromPackageResponse400
    | GetProductsFromPackageResponse401
    | GetProductsFromPackageResponse403
    | GetProductsFromPackageResponse404
    | GetProductsFromPackageResponse423
    | GetProductsFromPackageResponse429
    | GetProductsFromPackageResponse500
    | GetProductsFromPackageResponse503
    | ProductsFromPackageList
]:
    """Get a list of products attached to a given package of an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductsFromPackageResponse400 | GetProductsFromPackageResponse401 | GetProductsFromPackageResponse403 | GetProductsFromPackageResponse404 | GetProductsFromPackageResponse423 | GetProductsFromPackageResponse429 | GetProductsFromPackageResponse500 | GetProductsFromPackageResponse503 | ProductsFromPackageList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        package_id=package_id,
        starting_after=starting_after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    GetProductsFromPackageResponse400
    | GetProductsFromPackageResponse401
    | GetProductsFromPackageResponse403
    | GetProductsFromPackageResponse404
    | GetProductsFromPackageResponse423
    | GetProductsFromPackageResponse429
    | GetProductsFromPackageResponse500
    | GetProductsFromPackageResponse503
    | ProductsFromPackageList
    | None
):
    """Get a list of products attached to a given package of an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductsFromPackageResponse400 | GetProductsFromPackageResponse401 | GetProductsFromPackageResponse403 | GetProductsFromPackageResponse404 | GetProductsFromPackageResponse423 | GetProductsFromPackageResponse429 | GetProductsFromPackageResponse500 | GetProductsFromPackageResponse503 | ProductsFromPackageList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            package_id=package_id,
            client=client,
            starting_after=starting_after,
            limit=limit,
        )
    ).parsed
