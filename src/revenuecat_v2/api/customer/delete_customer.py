from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_customer_response_400 import DeleteCustomerResponse400
from ...models.delete_customer_response_401 import DeleteCustomerResponse401
from ...models.delete_customer_response_403 import DeleteCustomerResponse403
from ...models.delete_customer_response_404 import DeleteCustomerResponse404
from ...models.delete_customer_response_409 import DeleteCustomerResponse409
from ...models.delete_customer_response_422 import DeleteCustomerResponse422
from ...models.delete_customer_response_423 import DeleteCustomerResponse423
from ...models.delete_customer_response_429 import DeleteCustomerResponse429
from ...models.delete_customer_response_500 import DeleteCustomerResponse500
from ...models.delete_customer_response_503 import DeleteCustomerResponse503
from ...models.deleted_object import DeletedObject
from ...types import Response


def _get_kwargs(
    project_id: str,
    customer_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/customers/{customer_id}".format(
            project_id=quote(str(project_id), safe=""),
            customer_id=quote(str(customer_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteCustomerResponse400
    | DeleteCustomerResponse401
    | DeleteCustomerResponse403
    | DeleteCustomerResponse404
    | DeleteCustomerResponse409
    | DeleteCustomerResponse422
    | DeleteCustomerResponse423
    | DeleteCustomerResponse429
    | DeleteCustomerResponse500
    | DeleteCustomerResponse503
    | DeletedObject
    | None
):
    if response.status_code == 200:
        response_200 = DeletedObject.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteCustomerResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteCustomerResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteCustomerResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteCustomerResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeleteCustomerResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = DeleteCustomerResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = DeleteCustomerResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = DeleteCustomerResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteCustomerResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteCustomerResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteCustomerResponse400
    | DeleteCustomerResponse401
    | DeleteCustomerResponse403
    | DeleteCustomerResponse404
    | DeleteCustomerResponse409
    | DeleteCustomerResponse422
    | DeleteCustomerResponse423
    | DeleteCustomerResponse429
    | DeleteCustomerResponse500
    | DeleteCustomerResponse503
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
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteCustomerResponse400
    | DeleteCustomerResponse401
    | DeleteCustomerResponse403
    | DeleteCustomerResponse404
    | DeleteCustomerResponse409
    | DeleteCustomerResponse422
    | DeleteCustomerResponse423
    | DeleteCustomerResponse429
    | DeleteCustomerResponse500
    | DeleteCustomerResponse503
    | DeletedObject
]:
    """Delete a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCustomerResponse400 | DeleteCustomerResponse401 | DeleteCustomerResponse403 | DeleteCustomerResponse404 | DeleteCustomerResponse409 | DeleteCustomerResponse422 | DeleteCustomerResponse423 | DeleteCustomerResponse429 | DeleteCustomerResponse500 | DeleteCustomerResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
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
) -> (
    DeleteCustomerResponse400
    | DeleteCustomerResponse401
    | DeleteCustomerResponse403
    | DeleteCustomerResponse404
    | DeleteCustomerResponse409
    | DeleteCustomerResponse422
    | DeleteCustomerResponse423
    | DeleteCustomerResponse429
    | DeleteCustomerResponse500
    | DeleteCustomerResponse503
    | DeletedObject
    | None
):
    """Delete a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCustomerResponse400 | DeleteCustomerResponse401 | DeleteCustomerResponse403 | DeleteCustomerResponse404 | DeleteCustomerResponse409 | DeleteCustomerResponse422 | DeleteCustomerResponse423 | DeleteCustomerResponse429 | DeleteCustomerResponse500 | DeleteCustomerResponse503 | DeletedObject
    """

    return sync_detailed(
        project_id=project_id,
        customer_id=customer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteCustomerResponse400
    | DeleteCustomerResponse401
    | DeleteCustomerResponse403
    | DeleteCustomerResponse404
    | DeleteCustomerResponse409
    | DeleteCustomerResponse422
    | DeleteCustomerResponse423
    | DeleteCustomerResponse429
    | DeleteCustomerResponse500
    | DeleteCustomerResponse503
    | DeletedObject
]:
    """Delete a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCustomerResponse400 | DeleteCustomerResponse401 | DeleteCustomerResponse403 | DeleteCustomerResponse404 | DeleteCustomerResponse409 | DeleteCustomerResponse422 | DeleteCustomerResponse423 | DeleteCustomerResponse429 | DeleteCustomerResponse500 | DeleteCustomerResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteCustomerResponse400
    | DeleteCustomerResponse401
    | DeleteCustomerResponse403
    | DeleteCustomerResponse404
    | DeleteCustomerResponse409
    | DeleteCustomerResponse422
    | DeleteCustomerResponse423
    | DeleteCustomerResponse429
    | DeleteCustomerResponse500
    | DeleteCustomerResponse503
    | DeletedObject
    | None
):
    """Delete a customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCustomerResponse400 | DeleteCustomerResponse401 | DeleteCustomerResponse403 | DeleteCustomerResponse404 | DeleteCustomerResponse409 | DeleteCustomerResponse422 | DeleteCustomerResponse423 | DeleteCustomerResponse429 | DeleteCustomerResponse500 | DeleteCustomerResponse503 | DeletedObject
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            customer_id=customer_id,
            client=client,
        )
    ).parsed
