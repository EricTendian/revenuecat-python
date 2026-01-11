from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_list import CustomerList
from ...models.list_customers_response_400 import ListCustomersResponse400
from ...models.list_customers_response_401 import ListCustomersResponse401
from ...models.list_customers_response_403 import ListCustomersResponse403
from ...models.list_customers_response_404 import ListCustomersResponse404
from ...models.list_customers_response_423 import ListCustomersResponse423
from ...models.list_customers_response_429 import ListCustomersResponse429
from ...models.list_customers_response_500 import ListCustomersResponse500
from ...models.list_customers_response_503 import ListCustomersResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    search: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["starting_after"] = starting_after

    params["limit"] = limit

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/customers".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CustomerList
    | ListCustomersResponse400
    | ListCustomersResponse401
    | ListCustomersResponse403
    | ListCustomersResponse404
    | ListCustomersResponse423
    | ListCustomersResponse429
    | ListCustomersResponse500
    | ListCustomersResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CustomerList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListCustomersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListCustomersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListCustomersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListCustomersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListCustomersResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListCustomersResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListCustomersResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListCustomersResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CustomerList
    | ListCustomersResponse400
    | ListCustomersResponse401
    | ListCustomersResponse403
    | ListCustomersResponse404
    | ListCustomersResponse423
    | ListCustomersResponse429
    | ListCustomersResponse500
    | ListCustomersResponse503
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
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    search: str | Unset = UNSET,
) -> Response[
    CustomerList
    | ListCustomersResponse400
    | ListCustomersResponse401
    | ListCustomersResponse403
    | ListCustomersResponse404
    | ListCustomersResponse423
    | ListCustomersResponse429
    | ListCustomersResponse500
    | ListCustomersResponse503
]:
    """Get a list of customers

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        search (str | Unset):  Example: example@example.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerList | ListCustomersResponse400 | ListCustomersResponse401 | ListCustomersResponse403 | ListCustomersResponse404 | ListCustomersResponse423 | ListCustomersResponse429 | ListCustomersResponse500 | ListCustomersResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        starting_after=starting_after,
        limit=limit,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    search: str | Unset = UNSET,
) -> (
    CustomerList
    | ListCustomersResponse400
    | ListCustomersResponse401
    | ListCustomersResponse403
    | ListCustomersResponse404
    | ListCustomersResponse423
    | ListCustomersResponse429
    | ListCustomersResponse500
    | ListCustomersResponse503
    | None
):
    """Get a list of customers

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        search (str | Unset):  Example: example@example.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerList | ListCustomersResponse400 | ListCustomersResponse401 | ListCustomersResponse403 | ListCustomersResponse404 | ListCustomersResponse423 | ListCustomersResponse429 | ListCustomersResponse500 | ListCustomersResponse503
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        starting_after=starting_after,
        limit=limit,
        search=search,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    search: str | Unset = UNSET,
) -> Response[
    CustomerList
    | ListCustomersResponse400
    | ListCustomersResponse401
    | ListCustomersResponse403
    | ListCustomersResponse404
    | ListCustomersResponse423
    | ListCustomersResponse429
    | ListCustomersResponse500
    | ListCustomersResponse503
]:
    """Get a list of customers

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        search (str | Unset):  Example: example@example.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerList | ListCustomersResponse400 | ListCustomersResponse401 | ListCustomersResponse403 | ListCustomersResponse404 | ListCustomersResponse423 | ListCustomersResponse429 | ListCustomersResponse500 | ListCustomersResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        starting_after=starting_after,
        limit=limit,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    search: str | Unset = UNSET,
) -> (
    CustomerList
    | ListCustomersResponse400
    | ListCustomersResponse401
    | ListCustomersResponse403
    | ListCustomersResponse404
    | ListCustomersResponse423
    | ListCustomersResponse429
    | ListCustomersResponse500
    | ListCustomersResponse503
    | None
):
    """Get a list of customers

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        search (str | Unset):  Example: example@example.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerList | ListCustomersResponse400 | ListCustomersResponse401 | ListCustomersResponse403 | ListCustomersResponse404 | ListCustomersResponse423 | ListCustomersResponse429 | ListCustomersResponse500 | ListCustomersResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            starting_after=starting_after,
            limit=limit,
            search=search,
        )
    ).parsed
