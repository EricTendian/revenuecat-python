from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_attribute_list import CustomerAttributeList
from ...models.set_customer_attributes_body import SetCustomerAttributesBody
from ...models.set_customer_attributes_response_400 import SetCustomerAttributesResponse400
from ...models.set_customer_attributes_response_401 import SetCustomerAttributesResponse401
from ...models.set_customer_attributes_response_403 import SetCustomerAttributesResponse403
from ...models.set_customer_attributes_response_404 import SetCustomerAttributesResponse404
from ...models.set_customer_attributes_response_409 import SetCustomerAttributesResponse409
from ...models.set_customer_attributes_response_422 import SetCustomerAttributesResponse422
from ...models.set_customer_attributes_response_423 import SetCustomerAttributesResponse423
from ...models.set_customer_attributes_response_429 import SetCustomerAttributesResponse429
from ...models.set_customer_attributes_response_500 import SetCustomerAttributesResponse500
from ...models.set_customer_attributes_response_503 import SetCustomerAttributesResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    customer_id: str,
    *,
    body: SetCustomerAttributesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/customers/{customer_id}/attributes".format(
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
    CustomerAttributeList
    | SetCustomerAttributesResponse400
    | SetCustomerAttributesResponse401
    | SetCustomerAttributesResponse403
    | SetCustomerAttributesResponse404
    | SetCustomerAttributesResponse409
    | SetCustomerAttributesResponse422
    | SetCustomerAttributesResponse423
    | SetCustomerAttributesResponse429
    | SetCustomerAttributesResponse500
    | SetCustomerAttributesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CustomerAttributeList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SetCustomerAttributesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetCustomerAttributesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SetCustomerAttributesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetCustomerAttributesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = SetCustomerAttributesResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = SetCustomerAttributesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = SetCustomerAttributesResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = SetCustomerAttributesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SetCustomerAttributesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SetCustomerAttributesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CustomerAttributeList
    | SetCustomerAttributesResponse400
    | SetCustomerAttributesResponse401
    | SetCustomerAttributesResponse403
    | SetCustomerAttributesResponse404
    | SetCustomerAttributesResponse409
    | SetCustomerAttributesResponse422
    | SetCustomerAttributesResponse423
    | SetCustomerAttributesResponse429
    | SetCustomerAttributesResponse500
    | SetCustomerAttributesResponse503
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
    body: SetCustomerAttributesBody,
) -> Response[
    CustomerAttributeList
    | SetCustomerAttributesResponse400
    | SetCustomerAttributesResponse401
    | SetCustomerAttributesResponse403
    | SetCustomerAttributesResponse404
    | SetCustomerAttributesResponse409
    | SetCustomerAttributesResponse422
    | SetCustomerAttributesResponse423
    | SetCustomerAttributesResponse429
    | SetCustomerAttributesResponse500
    | SetCustomerAttributesResponse503
]:
    """Set a customer's attributes

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (SetCustomerAttributesBody):  Example: {'attributes': [{'name': '$email', 'value':
            'support@revenuecat.com'}, {'name': '$displayName', 'value': 'John Appleseed'}, {'name':
            'my_custom_attr', 'value': 'custom value'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerAttributeList | SetCustomerAttributesResponse400 | SetCustomerAttributesResponse401 | SetCustomerAttributesResponse403 | SetCustomerAttributesResponse404 | SetCustomerAttributesResponse409 | SetCustomerAttributesResponse422 | SetCustomerAttributesResponse423 | SetCustomerAttributesResponse429 | SetCustomerAttributesResponse500 | SetCustomerAttributesResponse503]
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
    body: SetCustomerAttributesBody,
) -> (
    CustomerAttributeList
    | SetCustomerAttributesResponse400
    | SetCustomerAttributesResponse401
    | SetCustomerAttributesResponse403
    | SetCustomerAttributesResponse404
    | SetCustomerAttributesResponse409
    | SetCustomerAttributesResponse422
    | SetCustomerAttributesResponse423
    | SetCustomerAttributesResponse429
    | SetCustomerAttributesResponse500
    | SetCustomerAttributesResponse503
    | None
):
    """Set a customer's attributes

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (SetCustomerAttributesBody):  Example: {'attributes': [{'name': '$email', 'value':
            'support@revenuecat.com'}, {'name': '$displayName', 'value': 'John Appleseed'}, {'name':
            'my_custom_attr', 'value': 'custom value'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerAttributeList | SetCustomerAttributesResponse400 | SetCustomerAttributesResponse401 | SetCustomerAttributesResponse403 | SetCustomerAttributesResponse404 | SetCustomerAttributesResponse409 | SetCustomerAttributesResponse422 | SetCustomerAttributesResponse423 | SetCustomerAttributesResponse429 | SetCustomerAttributesResponse500 | SetCustomerAttributesResponse503
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
    body: SetCustomerAttributesBody,
) -> Response[
    CustomerAttributeList
    | SetCustomerAttributesResponse400
    | SetCustomerAttributesResponse401
    | SetCustomerAttributesResponse403
    | SetCustomerAttributesResponse404
    | SetCustomerAttributesResponse409
    | SetCustomerAttributesResponse422
    | SetCustomerAttributesResponse423
    | SetCustomerAttributesResponse429
    | SetCustomerAttributesResponse500
    | SetCustomerAttributesResponse503
]:
    """Set a customer's attributes

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (SetCustomerAttributesBody):  Example: {'attributes': [{'name': '$email', 'value':
            'support@revenuecat.com'}, {'name': '$displayName', 'value': 'John Appleseed'}, {'name':
            'my_custom_attr', 'value': 'custom value'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerAttributeList | SetCustomerAttributesResponse400 | SetCustomerAttributesResponse401 | SetCustomerAttributesResponse403 | SetCustomerAttributesResponse404 | SetCustomerAttributesResponse409 | SetCustomerAttributesResponse422 | SetCustomerAttributesResponse423 | SetCustomerAttributesResponse429 | SetCustomerAttributesResponse500 | SetCustomerAttributesResponse503]
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
    body: SetCustomerAttributesBody,
) -> (
    CustomerAttributeList
    | SetCustomerAttributesResponse400
    | SetCustomerAttributesResponse401
    | SetCustomerAttributesResponse403
    | SetCustomerAttributesResponse404
    | SetCustomerAttributesResponse409
    | SetCustomerAttributesResponse422
    | SetCustomerAttributesResponse423
    | SetCustomerAttributesResponse429
    | SetCustomerAttributesResponse500
    | SetCustomerAttributesResponse503
    | None
):
    """Set a customer's attributes

     This endpoint requires the following permission(s):
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (SetCustomerAttributesBody):  Example: {'attributes': [{'name': '$email', 'value':
            'support@revenuecat.com'}, {'name': '$displayName', 'value': 'John Appleseed'}, {'name':
            'my_custom_attr', 'value': 'custom value'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerAttributeList | SetCustomerAttributesResponse400 | SetCustomerAttributesResponse401 | SetCustomerAttributesResponse403 | SetCustomerAttributesResponse404 | SetCustomerAttributesResponse409 | SetCustomerAttributesResponse422 | SetCustomerAttributesResponse423 | SetCustomerAttributesResponse429 | SetCustomerAttributesResponse500 | SetCustomerAttributesResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            customer_id=customer_id,
            client=client,
            body=body,
        )
    ).parsed
