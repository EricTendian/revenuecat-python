from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_invoices_list import CustomerInvoicesList
from ...models.list_customer_invoices_response_400 import ListCustomerInvoicesResponse400
from ...models.list_customer_invoices_response_401 import ListCustomerInvoicesResponse401
from ...models.list_customer_invoices_response_403 import ListCustomerInvoicesResponse403
from ...models.list_customer_invoices_response_404 import ListCustomerInvoicesResponse404
from ...models.list_customer_invoices_response_423 import ListCustomerInvoicesResponse423
from ...models.list_customer_invoices_response_429 import ListCustomerInvoicesResponse429
from ...models.list_customer_invoices_response_500 import ListCustomerInvoicesResponse500
from ...models.list_customer_invoices_response_503 import ListCustomerInvoicesResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    customer_id: str,
    *,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["starting_after"] = starting_after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/customers/{customer_id}/invoices".format(
            project_id=quote(str(project_id), safe=""),
            customer_id=quote(str(customer_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CustomerInvoicesList
    | ListCustomerInvoicesResponse400
    | ListCustomerInvoicesResponse401
    | ListCustomerInvoicesResponse403
    | ListCustomerInvoicesResponse404
    | ListCustomerInvoicesResponse423
    | ListCustomerInvoicesResponse429
    | ListCustomerInvoicesResponse500
    | ListCustomerInvoicesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CustomerInvoicesList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListCustomerInvoicesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListCustomerInvoicesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListCustomerInvoicesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListCustomerInvoicesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListCustomerInvoicesResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListCustomerInvoicesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListCustomerInvoicesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListCustomerInvoicesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CustomerInvoicesList
    | ListCustomerInvoicesResponse400
    | ListCustomerInvoicesResponse401
    | ListCustomerInvoicesResponse403
    | ListCustomerInvoicesResponse404
    | ListCustomerInvoicesResponse423
    | ListCustomerInvoicesResponse429
    | ListCustomerInvoicesResponse500
    | ListCustomerInvoicesResponse503
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
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    CustomerInvoicesList
    | ListCustomerInvoicesResponse400
    | ListCustomerInvoicesResponse401
    | ListCustomerInvoicesResponse403
    | ListCustomerInvoicesResponse404
    | ListCustomerInvoicesResponse423
    | ListCustomerInvoicesResponse429
    | ListCustomerInvoicesResponse500
    | ListCustomerInvoicesResponse503
]:
    """Get a list of the customer's invoices

     This endpoint requires the following permission(s): <code>customer_information:invoices:read</code>.
    This endpoint belongs to the <strong>Customer Information</strong> domain, which has a default rate
    limit of <strong>480 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerInvoicesList | ListCustomerInvoicesResponse400 | ListCustomerInvoicesResponse401 | ListCustomerInvoicesResponse403 | ListCustomerInvoicesResponse404 | ListCustomerInvoicesResponse423 | ListCustomerInvoicesResponse429 | ListCustomerInvoicesResponse500 | ListCustomerInvoicesResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        starting_after=starting_after,
        limit=limit,
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
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    CustomerInvoicesList
    | ListCustomerInvoicesResponse400
    | ListCustomerInvoicesResponse401
    | ListCustomerInvoicesResponse403
    | ListCustomerInvoicesResponse404
    | ListCustomerInvoicesResponse423
    | ListCustomerInvoicesResponse429
    | ListCustomerInvoicesResponse500
    | ListCustomerInvoicesResponse503
    | None
):
    """Get a list of the customer's invoices

     This endpoint requires the following permission(s): <code>customer_information:invoices:read</code>.
    This endpoint belongs to the <strong>Customer Information</strong> domain, which has a default rate
    limit of <strong>480 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerInvoicesList | ListCustomerInvoicesResponse400 | ListCustomerInvoicesResponse401 | ListCustomerInvoicesResponse403 | ListCustomerInvoicesResponse404 | ListCustomerInvoicesResponse423 | ListCustomerInvoicesResponse429 | ListCustomerInvoicesResponse500 | ListCustomerInvoicesResponse503
    """

    return sync_detailed(
        project_id=project_id,
        customer_id=customer_id,
        client=client,
        starting_after=starting_after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    CustomerInvoicesList
    | ListCustomerInvoicesResponse400
    | ListCustomerInvoicesResponse401
    | ListCustomerInvoicesResponse403
    | ListCustomerInvoicesResponse404
    | ListCustomerInvoicesResponse423
    | ListCustomerInvoicesResponse429
    | ListCustomerInvoicesResponse500
    | ListCustomerInvoicesResponse503
]:
    """Get a list of the customer's invoices

     This endpoint requires the following permission(s): <code>customer_information:invoices:read</code>.
    This endpoint belongs to the <strong>Customer Information</strong> domain, which has a default rate
    limit of <strong>480 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerInvoicesList | ListCustomerInvoicesResponse400 | ListCustomerInvoicesResponse401 | ListCustomerInvoicesResponse403 | ListCustomerInvoicesResponse404 | ListCustomerInvoicesResponse423 | ListCustomerInvoicesResponse429 | ListCustomerInvoicesResponse500 | ListCustomerInvoicesResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        starting_after=starting_after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    CustomerInvoicesList
    | ListCustomerInvoicesResponse400
    | ListCustomerInvoicesResponse401
    | ListCustomerInvoicesResponse403
    | ListCustomerInvoicesResponse404
    | ListCustomerInvoicesResponse423
    | ListCustomerInvoicesResponse429
    | ListCustomerInvoicesResponse500
    | ListCustomerInvoicesResponse503
    | None
):
    """Get a list of the customer's invoices

     This endpoint requires the following permission(s): <code>customer_information:invoices:read</code>.
    This endpoint belongs to the <strong>Customer Information</strong> domain, which has a default rate
    limit of <strong>480 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerInvoicesList | ListCustomerInvoicesResponse400 | ListCustomerInvoicesResponse401 | ListCustomerInvoicesResponse403 | ListCustomerInvoicesResponse404 | ListCustomerInvoicesResponse423 | ListCustomerInvoicesResponse429 | ListCustomerInvoicesResponse500 | ListCustomerInvoicesResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            customer_id=customer_id,
            client=client,
            starting_after=starting_after,
            limit=limit,
        )
    ).parsed
