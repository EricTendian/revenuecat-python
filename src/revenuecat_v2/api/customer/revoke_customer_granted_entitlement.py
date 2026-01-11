from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer import Customer
from ...models.revoke_customer_granted_entitlement_body import RevokeCustomerGrantedEntitlementBody
from ...models.revoke_customer_granted_entitlement_response_400 import RevokeCustomerGrantedEntitlementResponse400
from ...models.revoke_customer_granted_entitlement_response_401 import RevokeCustomerGrantedEntitlementResponse401
from ...models.revoke_customer_granted_entitlement_response_403 import RevokeCustomerGrantedEntitlementResponse403
from ...models.revoke_customer_granted_entitlement_response_404 import RevokeCustomerGrantedEntitlementResponse404
from ...models.revoke_customer_granted_entitlement_response_409 import RevokeCustomerGrantedEntitlementResponse409
from ...models.revoke_customer_granted_entitlement_response_422 import RevokeCustomerGrantedEntitlementResponse422
from ...models.revoke_customer_granted_entitlement_response_423 import RevokeCustomerGrantedEntitlementResponse423
from ...models.revoke_customer_granted_entitlement_response_429 import RevokeCustomerGrantedEntitlementResponse429
from ...models.revoke_customer_granted_entitlement_response_500 import RevokeCustomerGrantedEntitlementResponse500
from ...models.revoke_customer_granted_entitlement_response_503 import RevokeCustomerGrantedEntitlementResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    customer_id: str,
    *,
    body: RevokeCustomerGrantedEntitlementBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/customers/{customer_id}/actions/revoke_granted_entitlement".format(
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
    Customer
    | RevokeCustomerGrantedEntitlementResponse400
    | RevokeCustomerGrantedEntitlementResponse401
    | RevokeCustomerGrantedEntitlementResponse403
    | RevokeCustomerGrantedEntitlementResponse404
    | RevokeCustomerGrantedEntitlementResponse409
    | RevokeCustomerGrantedEntitlementResponse422
    | RevokeCustomerGrantedEntitlementResponse423
    | RevokeCustomerGrantedEntitlementResponse429
    | RevokeCustomerGrantedEntitlementResponse500
    | RevokeCustomerGrantedEntitlementResponse503
    | None
):
    if response.status_code == 200:
        response_200 = Customer.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RevokeCustomerGrantedEntitlementResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RevokeCustomerGrantedEntitlementResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RevokeCustomerGrantedEntitlementResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RevokeCustomerGrantedEntitlementResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = RevokeCustomerGrantedEntitlementResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = RevokeCustomerGrantedEntitlementResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = RevokeCustomerGrantedEntitlementResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = RevokeCustomerGrantedEntitlementResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RevokeCustomerGrantedEntitlementResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RevokeCustomerGrantedEntitlementResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Customer
    | RevokeCustomerGrantedEntitlementResponse400
    | RevokeCustomerGrantedEntitlementResponse401
    | RevokeCustomerGrantedEntitlementResponse403
    | RevokeCustomerGrantedEntitlementResponse404
    | RevokeCustomerGrantedEntitlementResponse409
    | RevokeCustomerGrantedEntitlementResponse422
    | RevokeCustomerGrantedEntitlementResponse423
    | RevokeCustomerGrantedEntitlementResponse429
    | RevokeCustomerGrantedEntitlementResponse500
    | RevokeCustomerGrantedEntitlementResponse503
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
    body: RevokeCustomerGrantedEntitlementBody,
) -> Response[
    Customer
    | RevokeCustomerGrantedEntitlementResponse400
    | RevokeCustomerGrantedEntitlementResponse401
    | RevokeCustomerGrantedEntitlementResponse403
    | RevokeCustomerGrantedEntitlementResponse404
    | RevokeCustomerGrantedEntitlementResponse409
    | RevokeCustomerGrantedEntitlementResponse422
    | RevokeCustomerGrantedEntitlementResponse423
    | RevokeCustomerGrantedEntitlementResponse429
    | RevokeCustomerGrantedEntitlementResponse500
    | RevokeCustomerGrantedEntitlementResponse503
]:
    """Revoke a granted entitlement from a customer. As a side effect, the promotional subscription
    associated with the granted entitlement is expired.

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (RevokeCustomerGrantedEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Customer | RevokeCustomerGrantedEntitlementResponse400 | RevokeCustomerGrantedEntitlementResponse401 | RevokeCustomerGrantedEntitlementResponse403 | RevokeCustomerGrantedEntitlementResponse404 | RevokeCustomerGrantedEntitlementResponse409 | RevokeCustomerGrantedEntitlementResponse422 | RevokeCustomerGrantedEntitlementResponse423 | RevokeCustomerGrantedEntitlementResponse429 | RevokeCustomerGrantedEntitlementResponse500 | RevokeCustomerGrantedEntitlementResponse503]
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
    body: RevokeCustomerGrantedEntitlementBody,
) -> (
    Customer
    | RevokeCustomerGrantedEntitlementResponse400
    | RevokeCustomerGrantedEntitlementResponse401
    | RevokeCustomerGrantedEntitlementResponse403
    | RevokeCustomerGrantedEntitlementResponse404
    | RevokeCustomerGrantedEntitlementResponse409
    | RevokeCustomerGrantedEntitlementResponse422
    | RevokeCustomerGrantedEntitlementResponse423
    | RevokeCustomerGrantedEntitlementResponse429
    | RevokeCustomerGrantedEntitlementResponse500
    | RevokeCustomerGrantedEntitlementResponse503
    | None
):
    """Revoke a granted entitlement from a customer. As a side effect, the promotional subscription
    associated with the granted entitlement is expired.

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (RevokeCustomerGrantedEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Customer | RevokeCustomerGrantedEntitlementResponse400 | RevokeCustomerGrantedEntitlementResponse401 | RevokeCustomerGrantedEntitlementResponse403 | RevokeCustomerGrantedEntitlementResponse404 | RevokeCustomerGrantedEntitlementResponse409 | RevokeCustomerGrantedEntitlementResponse422 | RevokeCustomerGrantedEntitlementResponse423 | RevokeCustomerGrantedEntitlementResponse429 | RevokeCustomerGrantedEntitlementResponse500 | RevokeCustomerGrantedEntitlementResponse503
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
    body: RevokeCustomerGrantedEntitlementBody,
) -> Response[
    Customer
    | RevokeCustomerGrantedEntitlementResponse400
    | RevokeCustomerGrantedEntitlementResponse401
    | RevokeCustomerGrantedEntitlementResponse403
    | RevokeCustomerGrantedEntitlementResponse404
    | RevokeCustomerGrantedEntitlementResponse409
    | RevokeCustomerGrantedEntitlementResponse422
    | RevokeCustomerGrantedEntitlementResponse423
    | RevokeCustomerGrantedEntitlementResponse429
    | RevokeCustomerGrantedEntitlementResponse500
    | RevokeCustomerGrantedEntitlementResponse503
]:
    """Revoke a granted entitlement from a customer. As a side effect, the promotional subscription
    associated with the granted entitlement is expired.

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (RevokeCustomerGrantedEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Customer | RevokeCustomerGrantedEntitlementResponse400 | RevokeCustomerGrantedEntitlementResponse401 | RevokeCustomerGrantedEntitlementResponse403 | RevokeCustomerGrantedEntitlementResponse404 | RevokeCustomerGrantedEntitlementResponse409 | RevokeCustomerGrantedEntitlementResponse422 | RevokeCustomerGrantedEntitlementResponse423 | RevokeCustomerGrantedEntitlementResponse429 | RevokeCustomerGrantedEntitlementResponse500 | RevokeCustomerGrantedEntitlementResponse503]
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
    body: RevokeCustomerGrantedEntitlementBody,
) -> (
    Customer
    | RevokeCustomerGrantedEntitlementResponse400
    | RevokeCustomerGrantedEntitlementResponse401
    | RevokeCustomerGrantedEntitlementResponse403
    | RevokeCustomerGrantedEntitlementResponse404
    | RevokeCustomerGrantedEntitlementResponse409
    | RevokeCustomerGrantedEntitlementResponse422
    | RevokeCustomerGrantedEntitlementResponse423
    | RevokeCustomerGrantedEntitlementResponse429
    | RevokeCustomerGrantedEntitlementResponse500
    | RevokeCustomerGrantedEntitlementResponse503
    | None
):
    """Revoke a granted entitlement from a customer. As a side effect, the promotional subscription
    associated with the granted entitlement is expired.

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (RevokeCustomerGrantedEntitlementBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Customer | RevokeCustomerGrantedEntitlementResponse400 | RevokeCustomerGrantedEntitlementResponse401 | RevokeCustomerGrantedEntitlementResponse403 | RevokeCustomerGrantedEntitlementResponse404 | RevokeCustomerGrantedEntitlementResponse409 | RevokeCustomerGrantedEntitlementResponse422 | RevokeCustomerGrantedEntitlementResponse423 | RevokeCustomerGrantedEntitlementResponse429 | RevokeCustomerGrantedEntitlementResponse500 | RevokeCustomerGrantedEntitlementResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            customer_id=customer_id,
            client=client,
            body=body,
        )
    ).parsed
