from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_product_response_400 import DeleteProductResponse400
from ...models.delete_product_response_401 import DeleteProductResponse401
from ...models.delete_product_response_403 import DeleteProductResponse403
from ...models.delete_product_response_404 import DeleteProductResponse404
from ...models.delete_product_response_409 import DeleteProductResponse409
from ...models.delete_product_response_422 import DeleteProductResponse422
from ...models.delete_product_response_423 import DeleteProductResponse423
from ...models.delete_product_response_429 import DeleteProductResponse429
from ...models.delete_product_response_500 import DeleteProductResponse500
from ...models.delete_product_response_503 import DeleteProductResponse503
from ...models.deleted_object import DeletedObject
from ...types import Response


def _get_kwargs(
    project_id: str,
    product_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/products/{product_id}".format(
            project_id=quote(str(project_id), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteProductResponse400
    | DeleteProductResponse401
    | DeleteProductResponse403
    | DeleteProductResponse404
    | DeleteProductResponse409
    | DeleteProductResponse422
    | DeleteProductResponse423
    | DeleteProductResponse429
    | DeleteProductResponse500
    | DeleteProductResponse503
    | DeletedObject
    | None
):
    if response.status_code == 200:
        response_200 = DeletedObject.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteProductResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteProductResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteProductResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteProductResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeleteProductResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = DeleteProductResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = DeleteProductResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = DeleteProductResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteProductResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteProductResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteProductResponse400
    | DeleteProductResponse401
    | DeleteProductResponse403
    | DeleteProductResponse404
    | DeleteProductResponse409
    | DeleteProductResponse422
    | DeleteProductResponse423
    | DeleteProductResponse429
    | DeleteProductResponse500
    | DeleteProductResponse503
    | DeletedObject
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
) -> Response[
    DeleteProductResponse400
    | DeleteProductResponse401
    | DeleteProductResponse403
    | DeleteProductResponse404
    | DeleteProductResponse409
    | DeleteProductResponse422
    | DeleteProductResponse423
    | DeleteProductResponse429
    | DeleteProductResponse500
    | DeleteProductResponse503
    | DeletedObject
]:
    """Delete a product

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProductResponse400 | DeleteProductResponse401 | DeleteProductResponse403 | DeleteProductResponse404 | DeleteProductResponse409 | DeleteProductResponse422 | DeleteProductResponse423 | DeleteProductResponse429 | DeleteProductResponse500 | DeleteProductResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        product_id=product_id,
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
) -> (
    DeleteProductResponse400
    | DeleteProductResponse401
    | DeleteProductResponse403
    | DeleteProductResponse404
    | DeleteProductResponse409
    | DeleteProductResponse422
    | DeleteProductResponse423
    | DeleteProductResponse429
    | DeleteProductResponse500
    | DeleteProductResponse503
    | DeletedObject
    | None
):
    """Delete a product

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProductResponse400 | DeleteProductResponse401 | DeleteProductResponse403 | DeleteProductResponse404 | DeleteProductResponse409 | DeleteProductResponse422 | DeleteProductResponse423 | DeleteProductResponse429 | DeleteProductResponse500 | DeleteProductResponse503 | DeletedObject
    """

    return sync_detailed(
        project_id=project_id,
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteProductResponse400
    | DeleteProductResponse401
    | DeleteProductResponse403
    | DeleteProductResponse404
    | DeleteProductResponse409
    | DeleteProductResponse422
    | DeleteProductResponse423
    | DeleteProductResponse429
    | DeleteProductResponse500
    | DeleteProductResponse503
    | DeletedObject
]:
    """Delete a product

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProductResponse400 | DeleteProductResponse401 | DeleteProductResponse403 | DeleteProductResponse404 | DeleteProductResponse409 | DeleteProductResponse422 | DeleteProductResponse423 | DeleteProductResponse429 | DeleteProductResponse500 | DeleteProductResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        product_id=product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteProductResponse400
    | DeleteProductResponse401
    | DeleteProductResponse403
    | DeleteProductResponse404
    | DeleteProductResponse409
    | DeleteProductResponse422
    | DeleteProductResponse423
    | DeleteProductResponse429
    | DeleteProductResponse500
    | DeleteProductResponse503
    | DeletedObject
    | None
):
    """Delete a product

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        product_id (str):  Example: prod1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProductResponse400 | DeleteProductResponse401 | DeleteProductResponse403 | DeleteProductResponse404 | DeleteProductResponse409 | DeleteProductResponse422 | DeleteProductResponse423 | DeleteProductResponse429 | DeleteProductResponse500 | DeleteProductResponse503 | DeletedObject
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            product_id=product_id,
            client=client,
        )
    ).parsed
