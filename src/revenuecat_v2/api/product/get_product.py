from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_product_expand_item import GetProductExpandItem
from ...models.get_product_response_400 import GetProductResponse400
from ...models.get_product_response_401 import GetProductResponse401
from ...models.get_product_response_403 import GetProductResponse403
from ...models.get_product_response_404 import GetProductResponse404
from ...models.get_product_response_423 import GetProductResponse423
from ...models.get_product_response_429 import GetProductResponse429
from ...models.get_product_response_500 import GetProductResponse500
from ...models.get_product_response_503 import GetProductResponse503
from ...models.product import Product
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    product_id: str,
    *,
    expand: list[GetProductExpandItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_expand: list[str] | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item = expand_item_data.value
            json_expand.append(expand_item)

    params["expand"] = json_expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/products/{product_id}".format(
            project_id=quote(str(project_id), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetProductResponse400
    | GetProductResponse401
    | GetProductResponse403
    | GetProductResponse404
    | GetProductResponse423
    | GetProductResponse429
    | GetProductResponse500
    | GetProductResponse503
    | Product
    | None
):
    if response.status_code == 200:
        response_200 = Product.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetProductResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetProductResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetProductResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetProductResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetProductResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetProductResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetProductResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetProductResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetProductResponse400
    | GetProductResponse401
    | GetProductResponse403
    | GetProductResponse404
    | GetProductResponse423
    | GetProductResponse429
    | GetProductResponse500
    | GetProductResponse503
    | Product
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetProductExpandItem] | Unset = UNSET,
) -> Response[
    GetProductResponse400
    | GetProductResponse401
    | GetProductResponse403
    | GetProductResponse404
    | GetProductResponse423
    | GetProductResponse429
    | GetProductResponse500
    | GetProductResponse503
    | Product
]:
    """Get a product

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.
        expand (list[GetProductExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductResponse400 | GetProductResponse401 | GetProductResponse403 | GetProductResponse404 | GetProductResponse423 | GetProductResponse429 | GetProductResponse500 | GetProductResponse503 | Product]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        product_id=product_id,
        expand=expand,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetProductExpandItem] | Unset = UNSET,
) -> (
    GetProductResponse400
    | GetProductResponse401
    | GetProductResponse403
    | GetProductResponse404
    | GetProductResponse423
    | GetProductResponse429
    | GetProductResponse500
    | GetProductResponse503
    | Product
    | None
):
    """Get a product

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.
        expand (list[GetProductExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductResponse400 | GetProductResponse401 | GetProductResponse403 | GetProductResponse404 | GetProductResponse423 | GetProductResponse429 | GetProductResponse500 | GetProductResponse503 | Product
    """

    return sync_detailed(
        project_id=project_id,
        product_id=product_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetProductExpandItem] | Unset = UNSET,
) -> Response[
    GetProductResponse400
    | GetProductResponse401
    | GetProductResponse403
    | GetProductResponse404
    | GetProductResponse423
    | GetProductResponse429
    | GetProductResponse500
    | GetProductResponse503
    | Product
]:
    """Get a product

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.
        expand (list[GetProductExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductResponse400 | GetProductResponse401 | GetProductResponse403 | GetProductResponse404 | GetProductResponse423 | GetProductResponse429 | GetProductResponse500 | GetProductResponse503 | Product]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        product_id=product_id,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetProductExpandItem] | Unset = UNSET,
) -> (
    GetProductResponse400
    | GetProductResponse401
    | GetProductResponse403
    | GetProductResponse404
    | GetProductResponse423
    | GetProductResponse429
    | GetProductResponse500
    | GetProductResponse503
    | Product
    | None
):
    """Get a product

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.
        expand (list[GetProductExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductResponse400 | GetProductResponse401 | GetProductResponse403 | GetProductResponse404 | GetProductResponse423 | GetProductResponse429 | GetProductResponse500 | GetProductResponse503 | Product
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            product_id=product_id,
            client=client,
            expand=expand,
        )
    ).parsed
