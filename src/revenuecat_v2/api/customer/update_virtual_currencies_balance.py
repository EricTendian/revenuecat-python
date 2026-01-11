from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_virtual_currencies_balance_body import UpdateVirtualCurrenciesBalanceBody
from ...models.update_virtual_currencies_balance_response_400 import UpdateVirtualCurrenciesBalanceResponse400
from ...models.update_virtual_currencies_balance_response_401 import UpdateVirtualCurrenciesBalanceResponse401
from ...models.update_virtual_currencies_balance_response_403 import UpdateVirtualCurrenciesBalanceResponse403
from ...models.update_virtual_currencies_balance_response_404 import UpdateVirtualCurrenciesBalanceResponse404
from ...models.update_virtual_currencies_balance_response_409 import UpdateVirtualCurrenciesBalanceResponse409
from ...models.update_virtual_currencies_balance_response_422 import UpdateVirtualCurrenciesBalanceResponse422
from ...models.update_virtual_currencies_balance_response_423 import UpdateVirtualCurrenciesBalanceResponse423
from ...models.update_virtual_currencies_balance_response_429 import UpdateVirtualCurrenciesBalanceResponse429
from ...models.update_virtual_currencies_balance_response_500 import UpdateVirtualCurrenciesBalanceResponse500
from ...models.update_virtual_currencies_balance_response_503 import UpdateVirtualCurrenciesBalanceResponse503
from ...models.virtual_currencies_balances_list import VirtualCurrenciesBalancesList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    customer_id: str,
    *,
    body: UpdateVirtualCurrenciesBalanceBody,
    include_empty_balances: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    params: dict[str, Any] = {}

    params["include_empty_balances"] = include_empty_balances

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/customers/{customer_id}/virtual_currencies/update_balance".format(
            project_id=quote(str(project_id), safe=""),
            customer_id=quote(str(customer_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateVirtualCurrenciesBalanceResponse400
    | UpdateVirtualCurrenciesBalanceResponse401
    | UpdateVirtualCurrenciesBalanceResponse403
    | UpdateVirtualCurrenciesBalanceResponse404
    | UpdateVirtualCurrenciesBalanceResponse409
    | UpdateVirtualCurrenciesBalanceResponse422
    | UpdateVirtualCurrenciesBalanceResponse423
    | UpdateVirtualCurrenciesBalanceResponse429
    | UpdateVirtualCurrenciesBalanceResponse500
    | UpdateVirtualCurrenciesBalanceResponse503
    | VirtualCurrenciesBalancesList
    | None
):
    if response.status_code == 200:
        response_200 = VirtualCurrenciesBalancesList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateVirtualCurrenciesBalanceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateVirtualCurrenciesBalanceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdateVirtualCurrenciesBalanceResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateVirtualCurrenciesBalanceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdateVirtualCurrenciesBalanceResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = UpdateVirtualCurrenciesBalanceResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = UpdateVirtualCurrenciesBalanceResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = UpdateVirtualCurrenciesBalanceResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateVirtualCurrenciesBalanceResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateVirtualCurrenciesBalanceResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateVirtualCurrenciesBalanceResponse400
    | UpdateVirtualCurrenciesBalanceResponse401
    | UpdateVirtualCurrenciesBalanceResponse403
    | UpdateVirtualCurrenciesBalanceResponse404
    | UpdateVirtualCurrenciesBalanceResponse409
    | UpdateVirtualCurrenciesBalanceResponse422
    | UpdateVirtualCurrenciesBalanceResponse423
    | UpdateVirtualCurrenciesBalanceResponse429
    | UpdateVirtualCurrenciesBalanceResponse500
    | UpdateVirtualCurrenciesBalanceResponse503
    | VirtualCurrenciesBalancesList
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
    body: UpdateVirtualCurrenciesBalanceBody,
    include_empty_balances: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    UpdateVirtualCurrenciesBalanceResponse400
    | UpdateVirtualCurrenciesBalanceResponse401
    | UpdateVirtualCurrenciesBalanceResponse403
    | UpdateVirtualCurrenciesBalanceResponse404
    | UpdateVirtualCurrenciesBalanceResponse409
    | UpdateVirtualCurrenciesBalanceResponse422
    | UpdateVirtualCurrenciesBalanceResponse423
    | UpdateVirtualCurrenciesBalanceResponse429
    | UpdateVirtualCurrenciesBalanceResponse500
    | UpdateVirtualCurrenciesBalanceResponse503
    | VirtualCurrenciesBalancesList
]:
    """Update a virtual currencies balance without creating a transaction

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the <strong>Virtual
    Currencies - Create Transaction</strong> domain, which has a default rate limit of <strong>480
    requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        include_empty_balances (bool | Unset):  Example: True.
        idempotency_key (str | Unset):  Example: 1234-5678-9101-1121.
        body (UpdateVirtualCurrenciesBalanceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateVirtualCurrenciesBalanceResponse400 | UpdateVirtualCurrenciesBalanceResponse401 | UpdateVirtualCurrenciesBalanceResponse403 | UpdateVirtualCurrenciesBalanceResponse404 | UpdateVirtualCurrenciesBalanceResponse409 | UpdateVirtualCurrenciesBalanceResponse422 | UpdateVirtualCurrenciesBalanceResponse423 | UpdateVirtualCurrenciesBalanceResponse429 | UpdateVirtualCurrenciesBalanceResponse500 | UpdateVirtualCurrenciesBalanceResponse503 | VirtualCurrenciesBalancesList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        body=body,
        include_empty_balances=include_empty_balances,
        idempotency_key=idempotency_key,
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
    body: UpdateVirtualCurrenciesBalanceBody,
    include_empty_balances: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    UpdateVirtualCurrenciesBalanceResponse400
    | UpdateVirtualCurrenciesBalanceResponse401
    | UpdateVirtualCurrenciesBalanceResponse403
    | UpdateVirtualCurrenciesBalanceResponse404
    | UpdateVirtualCurrenciesBalanceResponse409
    | UpdateVirtualCurrenciesBalanceResponse422
    | UpdateVirtualCurrenciesBalanceResponse423
    | UpdateVirtualCurrenciesBalanceResponse429
    | UpdateVirtualCurrenciesBalanceResponse500
    | UpdateVirtualCurrenciesBalanceResponse503
    | VirtualCurrenciesBalancesList
    | None
):
    """Update a virtual currencies balance without creating a transaction

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the <strong>Virtual
    Currencies - Create Transaction</strong> domain, which has a default rate limit of <strong>480
    requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        include_empty_balances (bool | Unset):  Example: True.
        idempotency_key (str | Unset):  Example: 1234-5678-9101-1121.
        body (UpdateVirtualCurrenciesBalanceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateVirtualCurrenciesBalanceResponse400 | UpdateVirtualCurrenciesBalanceResponse401 | UpdateVirtualCurrenciesBalanceResponse403 | UpdateVirtualCurrenciesBalanceResponse404 | UpdateVirtualCurrenciesBalanceResponse409 | UpdateVirtualCurrenciesBalanceResponse422 | UpdateVirtualCurrenciesBalanceResponse423 | UpdateVirtualCurrenciesBalanceResponse429 | UpdateVirtualCurrenciesBalanceResponse500 | UpdateVirtualCurrenciesBalanceResponse503 | VirtualCurrenciesBalancesList
    """

    return sync_detailed(
        project_id=project_id,
        customer_id=customer_id,
        client=client,
        body=body,
        include_empty_balances=include_empty_balances,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVirtualCurrenciesBalanceBody,
    include_empty_balances: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    UpdateVirtualCurrenciesBalanceResponse400
    | UpdateVirtualCurrenciesBalanceResponse401
    | UpdateVirtualCurrenciesBalanceResponse403
    | UpdateVirtualCurrenciesBalanceResponse404
    | UpdateVirtualCurrenciesBalanceResponse409
    | UpdateVirtualCurrenciesBalanceResponse422
    | UpdateVirtualCurrenciesBalanceResponse423
    | UpdateVirtualCurrenciesBalanceResponse429
    | UpdateVirtualCurrenciesBalanceResponse500
    | UpdateVirtualCurrenciesBalanceResponse503
    | VirtualCurrenciesBalancesList
]:
    """Update a virtual currencies balance without creating a transaction

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the <strong>Virtual
    Currencies - Create Transaction</strong> domain, which has a default rate limit of <strong>480
    requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        include_empty_balances (bool | Unset):  Example: True.
        idempotency_key (str | Unset):  Example: 1234-5678-9101-1121.
        body (UpdateVirtualCurrenciesBalanceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateVirtualCurrenciesBalanceResponse400 | UpdateVirtualCurrenciesBalanceResponse401 | UpdateVirtualCurrenciesBalanceResponse403 | UpdateVirtualCurrenciesBalanceResponse404 | UpdateVirtualCurrenciesBalanceResponse409 | UpdateVirtualCurrenciesBalanceResponse422 | UpdateVirtualCurrenciesBalanceResponse423 | UpdateVirtualCurrenciesBalanceResponse429 | UpdateVirtualCurrenciesBalanceResponse500 | UpdateVirtualCurrenciesBalanceResponse503 | VirtualCurrenciesBalancesList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        body=body,
        include_empty_balances=include_empty_balances,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVirtualCurrenciesBalanceBody,
    include_empty_balances: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    UpdateVirtualCurrenciesBalanceResponse400
    | UpdateVirtualCurrenciesBalanceResponse401
    | UpdateVirtualCurrenciesBalanceResponse403
    | UpdateVirtualCurrenciesBalanceResponse404
    | UpdateVirtualCurrenciesBalanceResponse409
    | UpdateVirtualCurrenciesBalanceResponse422
    | UpdateVirtualCurrenciesBalanceResponse423
    | UpdateVirtualCurrenciesBalanceResponse429
    | UpdateVirtualCurrenciesBalanceResponse500
    | UpdateVirtualCurrenciesBalanceResponse503
    | VirtualCurrenciesBalancesList
    | None
):
    """Update a virtual currencies balance without creating a transaction

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the <strong>Virtual
    Currencies - Create Transaction</strong> domain, which has a default rate limit of <strong>480
    requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        include_empty_balances (bool | Unset):  Example: True.
        idempotency_key (str | Unset):  Example: 1234-5678-9101-1121.
        body (UpdateVirtualCurrenciesBalanceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateVirtualCurrenciesBalanceResponse400 | UpdateVirtualCurrenciesBalanceResponse401 | UpdateVirtualCurrenciesBalanceResponse403 | UpdateVirtualCurrenciesBalanceResponse404 | UpdateVirtualCurrenciesBalanceResponse409 | UpdateVirtualCurrenciesBalanceResponse422 | UpdateVirtualCurrenciesBalanceResponse423 | UpdateVirtualCurrenciesBalanceResponse429 | UpdateVirtualCurrenciesBalanceResponse500 | UpdateVirtualCurrenciesBalanceResponse503 | VirtualCurrenciesBalancesList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            customer_id=customer_id,
            client=client,
            body=body,
            include_empty_balances=include_empty_balances,
            idempotency_key=idempotency_key,
        )
    ).parsed
