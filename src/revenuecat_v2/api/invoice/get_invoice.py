from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_invoice_response_400 import GetInvoiceResponse400
from ...models.get_invoice_response_401 import GetInvoiceResponse401
from ...models.get_invoice_response_403 import GetInvoiceResponse403
from ...models.get_invoice_response_404 import GetInvoiceResponse404
from ...models.get_invoice_response_423 import GetInvoiceResponse423
from ...models.get_invoice_response_429 import GetInvoiceResponse429
from ...models.get_invoice_response_500 import GetInvoiceResponse500
from ...models.get_invoice_response_503 import GetInvoiceResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    customer_id: str,
    invoice_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/customers/{customer_id}/invoices/{invoice_id}/file".format(
            project_id=quote(str(project_id), safe=""),
            customer_id=quote(str(customer_id), safe=""),
            invoice_id=quote(str(invoice_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetInvoiceResponse400
    | GetInvoiceResponse401
    | GetInvoiceResponse403
    | GetInvoiceResponse404
    | GetInvoiceResponse423
    | GetInvoiceResponse429
    | GetInvoiceResponse500
    | GetInvoiceResponse503
    | None
):
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 400:
        response_400 = GetInvoiceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetInvoiceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetInvoiceResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetInvoiceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetInvoiceResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetInvoiceResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetInvoiceResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetInvoiceResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetInvoiceResponse400
    | GetInvoiceResponse401
    | GetInvoiceResponse403
    | GetInvoiceResponse404
    | GetInvoiceResponse423
    | GetInvoiceResponse429
    | GetInvoiceResponse500
    | GetInvoiceResponse503
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
    invoice_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetInvoiceResponse400
    | GetInvoiceResponse401
    | GetInvoiceResponse403
    | GetInvoiceResponse404
    | GetInvoiceResponse423
    | GetInvoiceResponse429
    | GetInvoiceResponse500
    | GetInvoiceResponse503
]:
    """Get an invoice

     This endpoint requires the following permission(s): <code>customer_information:invoices:read</code>.
    This endpoint belongs to the <strong>Customer Information</strong> domain, which has a default rate
    limit of <strong>480 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        invoice_id (str):  Example: rcbin1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetInvoiceResponse400 | GetInvoiceResponse401 | GetInvoiceResponse403 | GetInvoiceResponse404 | GetInvoiceResponse423 | GetInvoiceResponse429 | GetInvoiceResponse500 | GetInvoiceResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        invoice_id=invoice_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    customer_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetInvoiceResponse400
    | GetInvoiceResponse401
    | GetInvoiceResponse403
    | GetInvoiceResponse404
    | GetInvoiceResponse423
    | GetInvoiceResponse429
    | GetInvoiceResponse500
    | GetInvoiceResponse503
    | None
):
    """Get an invoice

     This endpoint requires the following permission(s): <code>customer_information:invoices:read</code>.
    This endpoint belongs to the <strong>Customer Information</strong> domain, which has a default rate
    limit of <strong>480 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        invoice_id (str):  Example: rcbin1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetInvoiceResponse400 | GetInvoiceResponse401 | GetInvoiceResponse403 | GetInvoiceResponse404 | GetInvoiceResponse423 | GetInvoiceResponse429 | GetInvoiceResponse500 | GetInvoiceResponse503
    """

    return sync_detailed(
        project_id=project_id,
        customer_id=customer_id,
        invoice_id=invoice_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    customer_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetInvoiceResponse400
    | GetInvoiceResponse401
    | GetInvoiceResponse403
    | GetInvoiceResponse404
    | GetInvoiceResponse423
    | GetInvoiceResponse429
    | GetInvoiceResponse500
    | GetInvoiceResponse503
]:
    """Get an invoice

     This endpoint requires the following permission(s): <code>customer_information:invoices:read</code>.
    This endpoint belongs to the <strong>Customer Information</strong> domain, which has a default rate
    limit of <strong>480 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        invoice_id (str):  Example: rcbin1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetInvoiceResponse400 | GetInvoiceResponse401 | GetInvoiceResponse403 | GetInvoiceResponse404 | GetInvoiceResponse423 | GetInvoiceResponse429 | GetInvoiceResponse500 | GetInvoiceResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        invoice_id=invoice_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    customer_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetInvoiceResponse400
    | GetInvoiceResponse401
    | GetInvoiceResponse403
    | GetInvoiceResponse404
    | GetInvoiceResponse423
    | GetInvoiceResponse429
    | GetInvoiceResponse500
    | GetInvoiceResponse503
    | None
):
    """Get an invoice

     This endpoint requires the following permission(s): <code>customer_information:invoices:read</code>.
    This endpoint belongs to the <strong>Customer Information</strong> domain, which has a default rate
    limit of <strong>480 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        invoice_id (str):  Example: rcbin1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetInvoiceResponse400 | GetInvoiceResponse401 | GetInvoiceResponse403 | GetInvoiceResponse404 | GetInvoiceResponse423 | GetInvoiceResponse429 | GetInvoiceResponse500 | GetInvoiceResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            customer_id=customer_id,
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
