from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transfer_customer_data_body import TransferCustomerDataBody
from ...models.transfer_customer_data_response_400 import TransferCustomerDataResponse400
from ...models.transfer_customer_data_response_401 import TransferCustomerDataResponse401
from ...models.transfer_customer_data_response_403 import TransferCustomerDataResponse403
from ...models.transfer_customer_data_response_404 import TransferCustomerDataResponse404
from ...models.transfer_customer_data_response_409 import TransferCustomerDataResponse409
from ...models.transfer_customer_data_response_422 import TransferCustomerDataResponse422
from ...models.transfer_customer_data_response_423 import TransferCustomerDataResponse423
from ...models.transfer_customer_data_response_429 import TransferCustomerDataResponse429
from ...models.transfer_customer_data_response_500 import TransferCustomerDataResponse500
from ...models.transfer_customer_data_response_503 import TransferCustomerDataResponse503
from ...models.transfer_result import TransferResult
from ...types import Response


def _get_kwargs(
    project_id: str,
    customer_id: str,
    *,
    body: TransferCustomerDataBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/customers/{customer_id}/actions/transfer".format(
            project_id=quote(str(project_id), safe=""),
            customer_id=quote(str(customer_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TransferCustomerDataResponse400
    | TransferCustomerDataResponse401
    | TransferCustomerDataResponse403
    | TransferCustomerDataResponse404
    | TransferCustomerDataResponse409
    | TransferCustomerDataResponse422
    | TransferCustomerDataResponse423
    | TransferCustomerDataResponse429
    | TransferCustomerDataResponse500
    | TransferCustomerDataResponse503
    | TransferResult
    | None
):
    if response.status_code == 200:
        response_200 = TransferResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TransferCustomerDataResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TransferCustomerDataResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = TransferCustomerDataResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TransferCustomerDataResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = TransferCustomerDataResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = TransferCustomerDataResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = TransferCustomerDataResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = TransferCustomerDataResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TransferCustomerDataResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TransferCustomerDataResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TransferCustomerDataResponse400
    | TransferCustomerDataResponse401
    | TransferCustomerDataResponse403
    | TransferCustomerDataResponse404
    | TransferCustomerDataResponse409
    | TransferCustomerDataResponse422
    | TransferCustomerDataResponse423
    | TransferCustomerDataResponse429
    | TransferCustomerDataResponse500
    | TransferCustomerDataResponse503
    | TransferResult
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
    body: TransferCustomerDataBody,
) -> Response[
    TransferCustomerDataResponse400
    | TransferCustomerDataResponse401
    | TransferCustomerDataResponse403
    | TransferCustomerDataResponse404
    | TransferCustomerDataResponse409
    | TransferCustomerDataResponse422
    | TransferCustomerDataResponse423
    | TransferCustomerDataResponse429
    | TransferCustomerDataResponse500
    | TransferCustomerDataResponse503
    | TransferResult
]:
    """Transfer customer's subscriptions and one-time purchases to another customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>,
    <code>customer_information:subscriptions:read_write</code>,
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (TransferCustomerDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransferCustomerDataResponse400 | TransferCustomerDataResponse401 | TransferCustomerDataResponse403 | TransferCustomerDataResponse404 | TransferCustomerDataResponse409 | TransferCustomerDataResponse422 | TransferCustomerDataResponse423 | TransferCustomerDataResponse429 | TransferCustomerDataResponse500 | TransferCustomerDataResponse503 | TransferResult]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        body=body,
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
    body: TransferCustomerDataBody,
) -> (
    TransferCustomerDataResponse400
    | TransferCustomerDataResponse401
    | TransferCustomerDataResponse403
    | TransferCustomerDataResponse404
    | TransferCustomerDataResponse409
    | TransferCustomerDataResponse422
    | TransferCustomerDataResponse423
    | TransferCustomerDataResponse429
    | TransferCustomerDataResponse500
    | TransferCustomerDataResponse503
    | TransferResult
    | None
):
    """Transfer customer's subscriptions and one-time purchases to another customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>,
    <code>customer_information:subscriptions:read_write</code>,
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (TransferCustomerDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransferCustomerDataResponse400 | TransferCustomerDataResponse401 | TransferCustomerDataResponse403 | TransferCustomerDataResponse404 | TransferCustomerDataResponse409 | TransferCustomerDataResponse422 | TransferCustomerDataResponse423 | TransferCustomerDataResponse429 | TransferCustomerDataResponse500 | TransferCustomerDataResponse503 | TransferResult
    """

    return sync_detailed(
        project_id=project_id,
        customer_id=customer_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TransferCustomerDataBody,
) -> Response[
    TransferCustomerDataResponse400
    | TransferCustomerDataResponse401
    | TransferCustomerDataResponse403
    | TransferCustomerDataResponse404
    | TransferCustomerDataResponse409
    | TransferCustomerDataResponse422
    | TransferCustomerDataResponse423
    | TransferCustomerDataResponse429
    | TransferCustomerDataResponse500
    | TransferCustomerDataResponse503
    | TransferResult
]:
    """Transfer customer's subscriptions and one-time purchases to another customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>,
    <code>customer_information:subscriptions:read_write</code>,
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (TransferCustomerDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransferCustomerDataResponse400 | TransferCustomerDataResponse401 | TransferCustomerDataResponse403 | TransferCustomerDataResponse404 | TransferCustomerDataResponse409 | TransferCustomerDataResponse422 | TransferCustomerDataResponse423 | TransferCustomerDataResponse429 | TransferCustomerDataResponse500 | TransferCustomerDataResponse503 | TransferResult]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TransferCustomerDataBody,
) -> (
    TransferCustomerDataResponse400
    | TransferCustomerDataResponse401
    | TransferCustomerDataResponse403
    | TransferCustomerDataResponse404
    | TransferCustomerDataResponse409
    | TransferCustomerDataResponse422
    | TransferCustomerDataResponse423
    | TransferCustomerDataResponse429
    | TransferCustomerDataResponse500
    | TransferCustomerDataResponse503
    | TransferResult
    | None
):
    """Transfer customer's subscriptions and one-time purchases to another customer

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>,
    <code>customer_information:subscriptions:read_write</code>,
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (TransferCustomerDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransferCustomerDataResponse400 | TransferCustomerDataResponse401 | TransferCustomerDataResponse403 | TransferCustomerDataResponse404 | TransferCustomerDataResponse409 | TransferCustomerDataResponse422 | TransferCustomerDataResponse423 | TransferCustomerDataResponse429 | TransferCustomerDataResponse500 | TransferCustomerDataResponse503 | TransferResult
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            customer_id=customer_id,
            client=client,
            body=body,
        )
    ).parsed
