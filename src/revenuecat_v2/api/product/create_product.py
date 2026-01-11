from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_product_body import CreateProductBody
from ...models.create_product_response_400 import CreateProductResponse400
from ...models.create_product_response_401 import CreateProductResponse401
from ...models.create_product_response_403 import CreateProductResponse403
from ...models.create_product_response_404 import CreateProductResponse404
from ...models.create_product_response_409 import CreateProductResponse409
from ...models.create_product_response_422 import CreateProductResponse422
from ...models.create_product_response_423 import CreateProductResponse423
from ...models.create_product_response_429 import CreateProductResponse429
from ...models.create_product_response_500 import CreateProductResponse500
from ...models.create_product_response_503 import CreateProductResponse503
from ...models.product import Product
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: CreateProductBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/products".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateProductResponse400
    | CreateProductResponse401
    | CreateProductResponse403
    | CreateProductResponse404
    | CreateProductResponse409
    | CreateProductResponse422
    | CreateProductResponse423
    | CreateProductResponse429
    | CreateProductResponse500
    | CreateProductResponse503
    | Product
    | None
):
    if response.status_code == 201:
        response_201 = Product.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateProductResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateProductResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreateProductResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateProductResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreateProductResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CreateProductResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = CreateProductResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = CreateProductResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateProductResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateProductResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateProductResponse400
    | CreateProductResponse401
    | CreateProductResponse403
    | CreateProductResponse404
    | CreateProductResponse409
    | CreateProductResponse422
    | CreateProductResponse423
    | CreateProductResponse429
    | CreateProductResponse500
    | CreateProductResponse503
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
    *,
    client: AuthenticatedClient | Client,
    body: CreateProductBody,
) -> Response[
    CreateProductResponse400
    | CreateProductResponse401
    | CreateProductResponse403
    | CreateProductResponse404
    | CreateProductResponse409
    | CreateProductResponse422
    | CreateProductResponse423
    | CreateProductResponse429
    | CreateProductResponse500
    | CreateProductResponse503
    | Product
]:
    r"""Create a product

     <div class=\"theme-admonition theme-admonition-info alert alert--warning\">
      <div class=\"heading\">Warning</div>
      <div>This endpoint does not allow to create Web Billing products.</div>
    This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProductResponse400 | CreateProductResponse401 | CreateProductResponse403 | CreateProductResponse404 | CreateProductResponse409 | CreateProductResponse422 | CreateProductResponse423 | CreateProductResponse429 | CreateProductResponse500 | CreateProductResponse503 | Product]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateProductBody,
) -> (
    CreateProductResponse400
    | CreateProductResponse401
    | CreateProductResponse403
    | CreateProductResponse404
    | CreateProductResponse409
    | CreateProductResponse422
    | CreateProductResponse423
    | CreateProductResponse429
    | CreateProductResponse500
    | CreateProductResponse503
    | Product
    | None
):
    r"""Create a product

     <div class=\"theme-admonition theme-admonition-info alert alert--warning\">
      <div class=\"heading\">Warning</div>
      <div>This endpoint does not allow to create Web Billing products.</div>
    This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProductResponse400 | CreateProductResponse401 | CreateProductResponse403 | CreateProductResponse404 | CreateProductResponse409 | CreateProductResponse422 | CreateProductResponse423 | CreateProductResponse429 | CreateProductResponse500 | CreateProductResponse503 | Product
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateProductBody,
) -> Response[
    CreateProductResponse400
    | CreateProductResponse401
    | CreateProductResponse403
    | CreateProductResponse404
    | CreateProductResponse409
    | CreateProductResponse422
    | CreateProductResponse423
    | CreateProductResponse429
    | CreateProductResponse500
    | CreateProductResponse503
    | Product
]:
    r"""Create a product

     <div class=\"theme-admonition theme-admonition-info alert alert--warning\">
      <div class=\"heading\">Warning</div>
      <div>This endpoint does not allow to create Web Billing products.</div>
    This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProductResponse400 | CreateProductResponse401 | CreateProductResponse403 | CreateProductResponse404 | CreateProductResponse409 | CreateProductResponse422 | CreateProductResponse423 | CreateProductResponse429 | CreateProductResponse500 | CreateProductResponse503 | Product]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateProductBody,
) -> (
    CreateProductResponse400
    | CreateProductResponse401
    | CreateProductResponse403
    | CreateProductResponse404
    | CreateProductResponse409
    | CreateProductResponse422
    | CreateProductResponse423
    | CreateProductResponse429
    | CreateProductResponse500
    | CreateProductResponse503
    | Product
    | None
):
    r"""Create a product

     <div class=\"theme-admonition theme-admonition-info alert alert--warning\">
      <div class=\"heading\">Warning</div>
      <div>This endpoint does not allow to create Web Billing products.</div>
    This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProductResponse400 | CreateProductResponse401 | CreateProductResponse403 | CreateProductResponse404 | CreateProductResponse409 | CreateProductResponse422 | CreateProductResponse423 | CreateProductResponse429 | CreateProductResponse500 | CreateProductResponse503 | Product
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
