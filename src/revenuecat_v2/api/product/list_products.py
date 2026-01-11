from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_products_expand_item import ListProductsExpandItem
from ...models.list_products_response_400 import ListProductsResponse400
from ...models.list_products_response_401 import ListProductsResponse401
from ...models.list_products_response_403 import ListProductsResponse403
from ...models.list_products_response_404 import ListProductsResponse404
from ...models.list_products_response_423 import ListProductsResponse423
from ...models.list_products_response_429 import ListProductsResponse429
from ...models.list_products_response_500 import ListProductsResponse500
from ...models.list_products_response_503 import ListProductsResponse503
from ...models.product_list import ProductList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    app_id: str | Unset = UNSET,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListProductsExpandItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["app_id"] = app_id

    params["starting_after"] = starting_after

    params["limit"] = limit

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
        "url": "/projects/{project_id}/products".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListProductsResponse400
    | ListProductsResponse401
    | ListProductsResponse403
    | ListProductsResponse404
    | ListProductsResponse423
    | ListProductsResponse429
    | ListProductsResponse500
    | ListProductsResponse503
    | ProductList
    | None
):
    if response.status_code == 200:
        response_200 = ProductList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListProductsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListProductsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListProductsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListProductsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListProductsResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListProductsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListProductsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListProductsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListProductsResponse400
    | ListProductsResponse401
    | ListProductsResponse403
    | ListProductsResponse404
    | ListProductsResponse423
    | ListProductsResponse429
    | ListProductsResponse500
    | ListProductsResponse503
    | ProductList
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
    app_id: str | Unset = UNSET,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListProductsExpandItem] | Unset = UNSET,
) -> Response[
    ListProductsResponse400
    | ListProductsResponse401
    | ListProductsResponse403
    | ListProductsResponse404
    | ListProductsResponse423
    | ListProductsResponse429
    | ListProductsResponse500
    | ListProductsResponse503
    | ProductList
]:
    """Get a list of products

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str | Unset):  Example: app1a2b3c4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListProductsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProductsResponse400 | ListProductsResponse401 | ListProductsResponse403 | ListProductsResponse404 | ListProductsResponse423 | ListProductsResponse429 | ListProductsResponse500 | ListProductsResponse503 | ProductList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        app_id=app_id,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListProductsExpandItem] | Unset = UNSET,
) -> (
    ListProductsResponse400
    | ListProductsResponse401
    | ListProductsResponse403
    | ListProductsResponse404
    | ListProductsResponse423
    | ListProductsResponse429
    | ListProductsResponse500
    | ListProductsResponse503
    | ProductList
    | None
):
    """Get a list of products

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str | Unset):  Example: app1a2b3c4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListProductsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListProductsResponse400 | ListProductsResponse401 | ListProductsResponse403 | ListProductsResponse404 | ListProductsResponse423 | ListProductsResponse429 | ListProductsResponse500 | ListProductsResponse503 | ProductList
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        app_id=app_id,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListProductsExpandItem] | Unset = UNSET,
) -> Response[
    ListProductsResponse400
    | ListProductsResponse401
    | ListProductsResponse403
    | ListProductsResponse404
    | ListProductsResponse423
    | ListProductsResponse429
    | ListProductsResponse500
    | ListProductsResponse503
    | ProductList
]:
    """Get a list of products

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str | Unset):  Example: app1a2b3c4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListProductsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProductsResponse400 | ListProductsResponse401 | ListProductsResponse403 | ListProductsResponse404 | ListProductsResponse423 | ListProductsResponse429 | ListProductsResponse500 | ListProductsResponse503 | ProductList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        app_id=app_id,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListProductsExpandItem] | Unset = UNSET,
) -> (
    ListProductsResponse400
    | ListProductsResponse401
    | ListProductsResponse403
    | ListProductsResponse404
    | ListProductsResponse423
    | ListProductsResponse429
    | ListProductsResponse500
    | ListProductsResponse503
    | ProductList
    | None
):
    """Get a list of products

     This endpoint requires the following permission(s):
    <code>project_configuration:products:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str | Unset):  Example: app1a2b3c4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListProductsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListProductsResponse400 | ListProductsResponse401 | ListProductsResponse403 | ListProductsResponse404 | ListProductsResponse423 | ListProductsResponse429 | ListProductsResponse500 | ListProductsResponse503 | ProductList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            app_id=app_id,
            starting_after=starting_after,
            limit=limit,
            expand=expand,
        )
    ).parsed
