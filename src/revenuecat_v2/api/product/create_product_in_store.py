from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_product_in_store_body import CreateProductInStoreBody
from ...models.create_product_in_store_response_201 import CreateProductInStoreResponse201
from ...models.create_product_in_store_response_400 import CreateProductInStoreResponse400
from ...models.create_product_in_store_response_401 import CreateProductInStoreResponse401
from ...models.create_product_in_store_response_403 import CreateProductInStoreResponse403
from ...models.create_product_in_store_response_404 import CreateProductInStoreResponse404
from ...models.create_product_in_store_response_409 import CreateProductInStoreResponse409
from ...models.create_product_in_store_response_422 import CreateProductInStoreResponse422
from ...models.create_product_in_store_response_423 import CreateProductInStoreResponse423
from ...models.create_product_in_store_response_429 import CreateProductInStoreResponse429
from ...models.create_product_in_store_response_500 import CreateProductInStoreResponse500
from ...models.create_product_in_store_response_503 import CreateProductInStoreResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    product_id: str,
    *,
    body: CreateProductInStoreBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/products/{product_id}/create_in_store".format(
            project_id=quote(str(project_id), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateProductInStoreResponse201
    | CreateProductInStoreResponse400
    | CreateProductInStoreResponse401
    | CreateProductInStoreResponse403
    | CreateProductInStoreResponse404
    | CreateProductInStoreResponse409
    | CreateProductInStoreResponse422
    | CreateProductInStoreResponse423
    | CreateProductInStoreResponse429
    | CreateProductInStoreResponse500
    | CreateProductInStoreResponse503
    | None
):
    if response.status_code == 201:
        response_201 = CreateProductInStoreResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateProductInStoreResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateProductInStoreResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreateProductInStoreResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateProductInStoreResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreateProductInStoreResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CreateProductInStoreResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = CreateProductInStoreResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = CreateProductInStoreResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateProductInStoreResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateProductInStoreResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateProductInStoreResponse201
    | CreateProductInStoreResponse400
    | CreateProductInStoreResponse401
    | CreateProductInStoreResponse403
    | CreateProductInStoreResponse404
    | CreateProductInStoreResponse409
    | CreateProductInStoreResponse422
    | CreateProductInStoreResponse423
    | CreateProductInStoreResponse429
    | CreateProductInStoreResponse500
    | CreateProductInStoreResponse503
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
    body: CreateProductInStoreBody | Unset = UNSET,
) -> Response[
    CreateProductInStoreResponse201
    | CreateProductInStoreResponse400
    | CreateProductInStoreResponse401
    | CreateProductInStoreResponse403
    | CreateProductInStoreResponse404
    | CreateProductInStoreResponse409
    | CreateProductInStoreResponse422
    | CreateProductInStoreResponse423
    | CreateProductInStoreResponse429
    | CreateProductInStoreResponse500
    | CreateProductInStoreResponse503
]:
    """Push a product to the store

     Push a product to the App Store.

    **For subscription products**: You must provide store information including duration and
    subscription group details.

    **For in-app purchase products** (consumable, non-consumable, non-renewing subscription): No request
    body is required.
     This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.
        body (CreateProductInStoreBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProductInStoreResponse201 | CreateProductInStoreResponse400 | CreateProductInStoreResponse401 | CreateProductInStoreResponse403 | CreateProductInStoreResponse404 | CreateProductInStoreResponse409 | CreateProductInStoreResponse422 | CreateProductInStoreResponse423 | CreateProductInStoreResponse429 | CreateProductInStoreResponse500 | CreateProductInStoreResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        product_id=product_id,
        body=body,
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
    body: CreateProductInStoreBody | Unset = UNSET,
) -> (
    CreateProductInStoreResponse201
    | CreateProductInStoreResponse400
    | CreateProductInStoreResponse401
    | CreateProductInStoreResponse403
    | CreateProductInStoreResponse404
    | CreateProductInStoreResponse409
    | CreateProductInStoreResponse422
    | CreateProductInStoreResponse423
    | CreateProductInStoreResponse429
    | CreateProductInStoreResponse500
    | CreateProductInStoreResponse503
    | None
):
    """Push a product to the store

     Push a product to the App Store.

    **For subscription products**: You must provide store information including duration and
    subscription group details.

    **For in-app purchase products** (consumable, non-consumable, non-renewing subscription): No request
    body is required.
     This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.
        body (CreateProductInStoreBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProductInStoreResponse201 | CreateProductInStoreResponse400 | CreateProductInStoreResponse401 | CreateProductInStoreResponse403 | CreateProductInStoreResponse404 | CreateProductInStoreResponse409 | CreateProductInStoreResponse422 | CreateProductInStoreResponse423 | CreateProductInStoreResponse429 | CreateProductInStoreResponse500 | CreateProductInStoreResponse503
    """

    return sync_detailed(
        project_id=project_id,
        product_id=product_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateProductInStoreBody | Unset = UNSET,
) -> Response[
    CreateProductInStoreResponse201
    | CreateProductInStoreResponse400
    | CreateProductInStoreResponse401
    | CreateProductInStoreResponse403
    | CreateProductInStoreResponse404
    | CreateProductInStoreResponse409
    | CreateProductInStoreResponse422
    | CreateProductInStoreResponse423
    | CreateProductInStoreResponse429
    | CreateProductInStoreResponse500
    | CreateProductInStoreResponse503
]:
    """Push a product to the store

     Push a product to the App Store.

    **For subscription products**: You must provide store information including duration and
    subscription group details.

    **For in-app purchase products** (consumable, non-consumable, non-renewing subscription): No request
    body is required.
     This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.
        body (CreateProductInStoreBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProductInStoreResponse201 | CreateProductInStoreResponse400 | CreateProductInStoreResponse401 | CreateProductInStoreResponse403 | CreateProductInStoreResponse404 | CreateProductInStoreResponse409 | CreateProductInStoreResponse422 | CreateProductInStoreResponse423 | CreateProductInStoreResponse429 | CreateProductInStoreResponse500 | CreateProductInStoreResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        product_id=product_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateProductInStoreBody | Unset = UNSET,
) -> (
    CreateProductInStoreResponse201
    | CreateProductInStoreResponse400
    | CreateProductInStoreResponse401
    | CreateProductInStoreResponse403
    | CreateProductInStoreResponse404
    | CreateProductInStoreResponse409
    | CreateProductInStoreResponse422
    | CreateProductInStoreResponse423
    | CreateProductInStoreResponse429
    | CreateProductInStoreResponse500
    | CreateProductInStoreResponse503
    | None
):
    """Push a product to the store

     Push a product to the App Store.

    **For subscription products**: You must provide store information including duration and
    subscription group details.

    **For in-app purchase products** (consumable, non-consumable, non-renewing subscription): No request
    body is required.
     This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.
        body (CreateProductInStoreBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProductInStoreResponse201 | CreateProductInStoreResponse400 | CreateProductInStoreResponse401 | CreateProductInStoreResponse403 | CreateProductInStoreResponse404 | CreateProductInStoreResponse409 | CreateProductInStoreResponse422 | CreateProductInStoreResponse423 | CreateProductInStoreResponse429 | CreateProductInStoreResponse500 | CreateProductInStoreResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            product_id=product_id,
            client=client,
            body=body,
        )
    ).parsed
