from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer import Customer
from ...models.get_customer_expand_item import GetCustomerExpandItem
from ...models.get_customer_response_400 import GetCustomerResponse400
from ...models.get_customer_response_401 import GetCustomerResponse401
from ...models.get_customer_response_403 import GetCustomerResponse403
from ...models.get_customer_response_404 import GetCustomerResponse404
from ...models.get_customer_response_423 import GetCustomerResponse423
from ...models.get_customer_response_429 import GetCustomerResponse429
from ...models.get_customer_response_500 import GetCustomerResponse500
from ...models.get_customer_response_503 import GetCustomerResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    customer_id: str,
    *,
    expand: list[GetCustomerExpandItem] | Unset = UNSET,
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
        "url": "/projects/{project_id}/customers/{customer_id}".format(
            project_id=quote(str(project_id), safe=""),
            customer_id=quote(str(customer_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Customer
    | GetCustomerResponse400
    | GetCustomerResponse401
    | GetCustomerResponse403
    | GetCustomerResponse404
    | GetCustomerResponse423
    | GetCustomerResponse429
    | GetCustomerResponse500
    | GetCustomerResponse503
    | None
):
    if response.status_code == 200:
        response_200 = Customer.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCustomerResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetCustomerResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCustomerResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCustomerResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetCustomerResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetCustomerResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetCustomerResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetCustomerResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Customer
    | GetCustomerResponse400
    | GetCustomerResponse401
    | GetCustomerResponse403
    | GetCustomerResponse404
    | GetCustomerResponse423
    | GetCustomerResponse429
    | GetCustomerResponse500
    | GetCustomerResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetCustomerExpandItem] | Unset = UNSET,
) -> Response[
    Customer
    | GetCustomerResponse400
    | GetCustomerResponse401
    | GetCustomerResponse403
    | GetCustomerResponse404
    | GetCustomerResponse423
    | GetCustomerResponse429
    | GetCustomerResponse500
    | GetCustomerResponse503
]:
    """Get a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        expand (list[GetCustomerExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Customer | GetCustomerResponse400 | GetCustomerResponse401 | GetCustomerResponse403 | GetCustomerResponse404 | GetCustomerResponse423 | GetCustomerResponse429 | GetCustomerResponse500 | GetCustomerResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        expand=expand,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetCustomerExpandItem] | Unset = UNSET,
) -> (
    Customer
    | GetCustomerResponse400
    | GetCustomerResponse401
    | GetCustomerResponse403
    | GetCustomerResponse404
    | GetCustomerResponse423
    | GetCustomerResponse429
    | GetCustomerResponse500
    | GetCustomerResponse503
    | None
):
    """Get a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        expand (list[GetCustomerExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Customer | GetCustomerResponse400 | GetCustomerResponse401 | GetCustomerResponse403 | GetCustomerResponse404 | GetCustomerResponse423 | GetCustomerResponse429 | GetCustomerResponse500 | GetCustomerResponse503
    """

    return sync_detailed(
        project_id=project_id,
        customer_id=customer_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetCustomerExpandItem] | Unset = UNSET,
) -> Response[
    Customer
    | GetCustomerResponse400
    | GetCustomerResponse401
    | GetCustomerResponse403
    | GetCustomerResponse404
    | GetCustomerResponse423
    | GetCustomerResponse429
    | GetCustomerResponse500
    | GetCustomerResponse503
]:
    """Get a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        expand (list[GetCustomerExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Customer | GetCustomerResponse400 | GetCustomerResponse401 | GetCustomerResponse403 | GetCustomerResponse404 | GetCustomerResponse423 | GetCustomerResponse429 | GetCustomerResponse500 | GetCustomerResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetCustomerExpandItem] | Unset = UNSET,
) -> (
    Customer
    | GetCustomerResponse400
    | GetCustomerResponse401
    | GetCustomerResponse403
    | GetCustomerResponse404
    | GetCustomerResponse423
    | GetCustomerResponse429
    | GetCustomerResponse500
    | GetCustomerResponse503
    | None
):
    """Get a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read</code>. This endpoint belongs to the <strong>Customer
    Information</strong> domain, which has a default rate limit of <strong>480 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        expand (list[GetCustomerExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Customer | GetCustomerResponse400 | GetCustomerResponse401 | GetCustomerResponse403 | GetCustomerResponse404 | GetCustomerResponse423 | GetCustomerResponse429 | GetCustomerResponse500 | GetCustomerResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            customer_id=customer_id,
            client=client,
            expand=expand,
        )
    ).parsed
