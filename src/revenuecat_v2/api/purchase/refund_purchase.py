from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.purchase import Purchase
from ...models.refund_purchase_response_400 import RefundPurchaseResponse400
from ...models.refund_purchase_response_401 import RefundPurchaseResponse401
from ...models.refund_purchase_response_403 import RefundPurchaseResponse403
from ...models.refund_purchase_response_404 import RefundPurchaseResponse404
from ...models.refund_purchase_response_409 import RefundPurchaseResponse409
from ...models.refund_purchase_response_422 import RefundPurchaseResponse422
from ...models.refund_purchase_response_423 import RefundPurchaseResponse423
from ...models.refund_purchase_response_429 import RefundPurchaseResponse429
from ...models.refund_purchase_response_500 import RefundPurchaseResponse500
from ...models.refund_purchase_response_503 import RefundPurchaseResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    purchase_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/purchases/{purchase_id}/actions/refund".format(
            project_id=quote(str(project_id), safe=""),
            purchase_id=quote(str(purchase_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Purchase
    | RefundPurchaseResponse400
    | RefundPurchaseResponse401
    | RefundPurchaseResponse403
    | RefundPurchaseResponse404
    | RefundPurchaseResponse409
    | RefundPurchaseResponse422
    | RefundPurchaseResponse423
    | RefundPurchaseResponse429
    | RefundPurchaseResponse500
    | RefundPurchaseResponse503
    | None
):
    if response.status_code == 200:
        response_200 = Purchase.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RefundPurchaseResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RefundPurchaseResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RefundPurchaseResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RefundPurchaseResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = RefundPurchaseResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = RefundPurchaseResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = RefundPurchaseResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = RefundPurchaseResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RefundPurchaseResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RefundPurchaseResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Purchase
    | RefundPurchaseResponse400
    | RefundPurchaseResponse401
    | RefundPurchaseResponse403
    | RefundPurchaseResponse404
    | RefundPurchaseResponse409
    | RefundPurchaseResponse422
    | RefundPurchaseResponse423
    | RefundPurchaseResponse429
    | RefundPurchaseResponse500
    | RefundPurchaseResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    purchase_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Purchase
    | RefundPurchaseResponse400
    | RefundPurchaseResponse401
    | RefundPurchaseResponse403
    | RefundPurchaseResponse404
    | RefundPurchaseResponse409
    | RefundPurchaseResponse422
    | RefundPurchaseResponse423
    | RefundPurchaseResponse429
    | RefundPurchaseResponse500
    | RefundPurchaseResponse503
]:
    """Refund a Web Billing purchase

     Refund a Web Billing purchase and revoke access to associated granted entitlements.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Purchase | RefundPurchaseResponse400 | RefundPurchaseResponse401 | RefundPurchaseResponse403 | RefundPurchaseResponse404 | RefundPurchaseResponse409 | RefundPurchaseResponse422 | RefundPurchaseResponse423 | RefundPurchaseResponse429 | RefundPurchaseResponse500 | RefundPurchaseResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        purchase_id=purchase_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    purchase_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Purchase
    | RefundPurchaseResponse400
    | RefundPurchaseResponse401
    | RefundPurchaseResponse403
    | RefundPurchaseResponse404
    | RefundPurchaseResponse409
    | RefundPurchaseResponse422
    | RefundPurchaseResponse423
    | RefundPurchaseResponse429
    | RefundPurchaseResponse500
    | RefundPurchaseResponse503
    | None
):
    """Refund a Web Billing purchase

     Refund a Web Billing purchase and revoke access to associated granted entitlements.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Purchase | RefundPurchaseResponse400 | RefundPurchaseResponse401 | RefundPurchaseResponse403 | RefundPurchaseResponse404 | RefundPurchaseResponse409 | RefundPurchaseResponse422 | RefundPurchaseResponse423 | RefundPurchaseResponse429 | RefundPurchaseResponse500 | RefundPurchaseResponse503
    """

    return sync_detailed(
        project_id=project_id,
        purchase_id=purchase_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    purchase_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Purchase
    | RefundPurchaseResponse400
    | RefundPurchaseResponse401
    | RefundPurchaseResponse403
    | RefundPurchaseResponse404
    | RefundPurchaseResponse409
    | RefundPurchaseResponse422
    | RefundPurchaseResponse423
    | RefundPurchaseResponse429
    | RefundPurchaseResponse500
    | RefundPurchaseResponse503
]:
    """Refund a Web Billing purchase

     Refund a Web Billing purchase and revoke access to associated granted entitlements.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Purchase | RefundPurchaseResponse400 | RefundPurchaseResponse401 | RefundPurchaseResponse403 | RefundPurchaseResponse404 | RefundPurchaseResponse409 | RefundPurchaseResponse422 | RefundPurchaseResponse423 | RefundPurchaseResponse429 | RefundPurchaseResponse500 | RefundPurchaseResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        purchase_id=purchase_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    purchase_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Purchase
    | RefundPurchaseResponse400
    | RefundPurchaseResponse401
    | RefundPurchaseResponse403
    | RefundPurchaseResponse404
    | RefundPurchaseResponse409
    | RefundPurchaseResponse422
    | RefundPurchaseResponse423
    | RefundPurchaseResponse429
    | RefundPurchaseResponse500
    | RefundPurchaseResponse503
    | None
):
    """Refund a Web Billing purchase

     Refund a Web Billing purchase and revoke access to associated granted entitlements.
     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Purchase | RefundPurchaseResponse400 | RefundPurchaseResponse401 | RefundPurchaseResponse403 | RefundPurchaseResponse404 | RefundPurchaseResponse409 | RefundPurchaseResponse422 | RefundPurchaseResponse423 | RefundPurchaseResponse429 | RefundPurchaseResponse500 | RefundPurchaseResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            purchase_id=purchase_id,
            client=client,
        )
    ).parsed
