from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_customer_body import CreateCustomerBody
from ...models.create_customer_response_400 import CreateCustomerResponse400
from ...models.create_customer_response_401 import CreateCustomerResponse401
from ...models.create_customer_response_403 import CreateCustomerResponse403
from ...models.create_customer_response_404 import CreateCustomerResponse404
from ...models.create_customer_response_409 import CreateCustomerResponse409
from ...models.create_customer_response_422 import CreateCustomerResponse422
from ...models.create_customer_response_423 import CreateCustomerResponse423
from ...models.create_customer_response_429 import CreateCustomerResponse429
from ...models.create_customer_response_500 import CreateCustomerResponse500
from ...models.create_customer_response_503 import CreateCustomerResponse503
from ...models.customer import Customer
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: CreateCustomerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/customers".format(
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
    CreateCustomerResponse400
    | CreateCustomerResponse401
    | CreateCustomerResponse403
    | CreateCustomerResponse404
    | CreateCustomerResponse409
    | CreateCustomerResponse422
    | CreateCustomerResponse423
    | CreateCustomerResponse429
    | CreateCustomerResponse500
    | CreateCustomerResponse503
    | Customer
    | None
):
    if response.status_code == 201:
        response_201 = Customer.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateCustomerResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateCustomerResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreateCustomerResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateCustomerResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreateCustomerResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CreateCustomerResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = CreateCustomerResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = CreateCustomerResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateCustomerResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateCustomerResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateCustomerResponse400
    | CreateCustomerResponse401
    | CreateCustomerResponse403
    | CreateCustomerResponse404
    | CreateCustomerResponse409
    | CreateCustomerResponse422
    | CreateCustomerResponse423
    | CreateCustomerResponse429
    | CreateCustomerResponse500
    | CreateCustomerResponse503
    | Customer
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
    body: CreateCustomerBody,
) -> Response[
    CreateCustomerResponse400
    | CreateCustomerResponse401
    | CreateCustomerResponse403
    | CreateCustomerResponse404
    | CreateCustomerResponse409
    | CreateCustomerResponse422
    | CreateCustomerResponse423
    | CreateCustomerResponse429
    | CreateCustomerResponse500
    | CreateCustomerResponse503
    | Customer
]:
    """Create a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateCustomerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCustomerResponse400 | CreateCustomerResponse401 | CreateCustomerResponse403 | CreateCustomerResponse404 | CreateCustomerResponse409 | CreateCustomerResponse422 | CreateCustomerResponse423 | CreateCustomerResponse429 | CreateCustomerResponse500 | CreateCustomerResponse503 | Customer]
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
    body: CreateCustomerBody,
) -> (
    CreateCustomerResponse400
    | CreateCustomerResponse401
    | CreateCustomerResponse403
    | CreateCustomerResponse404
    | CreateCustomerResponse409
    | CreateCustomerResponse422
    | CreateCustomerResponse423
    | CreateCustomerResponse429
    | CreateCustomerResponse500
    | CreateCustomerResponse503
    | Customer
    | None
):
    """Create a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateCustomerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCustomerResponse400 | CreateCustomerResponse401 | CreateCustomerResponse403 | CreateCustomerResponse404 | CreateCustomerResponse409 | CreateCustomerResponse422 | CreateCustomerResponse423 | CreateCustomerResponse429 | CreateCustomerResponse500 | CreateCustomerResponse503 | Customer
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
    body: CreateCustomerBody,
) -> Response[
    CreateCustomerResponse400
    | CreateCustomerResponse401
    | CreateCustomerResponse403
    | CreateCustomerResponse404
    | CreateCustomerResponse409
    | CreateCustomerResponse422
    | CreateCustomerResponse423
    | CreateCustomerResponse429
    | CreateCustomerResponse500
    | CreateCustomerResponse503
    | Customer
]:
    """Create a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateCustomerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCustomerResponse400 | CreateCustomerResponse401 | CreateCustomerResponse403 | CreateCustomerResponse404 | CreateCustomerResponse409 | CreateCustomerResponse422 | CreateCustomerResponse423 | CreateCustomerResponse429 | CreateCustomerResponse500 | CreateCustomerResponse503 | Customer]
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
    body: CreateCustomerBody,
) -> (
    CreateCustomerResponse400
    | CreateCustomerResponse401
    | CreateCustomerResponse403
    | CreateCustomerResponse404
    | CreateCustomerResponse409
    | CreateCustomerResponse422
    | CreateCustomerResponse423
    | CreateCustomerResponse429
    | CreateCustomerResponse500
    | CreateCustomerResponse503
    | Customer
    | None
):
    """Create a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateCustomerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCustomerResponse400 | CreateCustomerResponse401 | CreateCustomerResponse403 | CreateCustomerResponse404 | CreateCustomerResponse409 | CreateCustomerResponse422 | CreateCustomerResponse423 | CreateCustomerResponse429 | CreateCustomerResponse500 | CreateCustomerResponse503 | Customer
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
