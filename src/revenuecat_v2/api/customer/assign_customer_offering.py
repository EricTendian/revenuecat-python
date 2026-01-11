from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assign_customer_offering_body import AssignCustomerOfferingBody
from ...models.assign_customer_offering_response_400 import AssignCustomerOfferingResponse400
from ...models.assign_customer_offering_response_401 import AssignCustomerOfferingResponse401
from ...models.assign_customer_offering_response_403 import AssignCustomerOfferingResponse403
from ...models.assign_customer_offering_response_404 import AssignCustomerOfferingResponse404
from ...models.assign_customer_offering_response_409 import AssignCustomerOfferingResponse409
from ...models.assign_customer_offering_response_422 import AssignCustomerOfferingResponse422
from ...models.assign_customer_offering_response_423 import AssignCustomerOfferingResponse423
from ...models.assign_customer_offering_response_429 import AssignCustomerOfferingResponse429
from ...models.assign_customer_offering_response_500 import AssignCustomerOfferingResponse500
from ...models.assign_customer_offering_response_503 import AssignCustomerOfferingResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    customer_id: str,
    *,
    body: AssignCustomerOfferingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/customers/{customer_id}/actions/assign_offering".format(
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
    Any
    | AssignCustomerOfferingResponse400
    | AssignCustomerOfferingResponse401
    | AssignCustomerOfferingResponse403
    | AssignCustomerOfferingResponse404
    | AssignCustomerOfferingResponse409
    | AssignCustomerOfferingResponse422
    | AssignCustomerOfferingResponse423
    | AssignCustomerOfferingResponse429
    | AssignCustomerOfferingResponse500
    | AssignCustomerOfferingResponse503
    | None
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = AssignCustomerOfferingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AssignCustomerOfferingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AssignCustomerOfferingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AssignCustomerOfferingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = AssignCustomerOfferingResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = AssignCustomerOfferingResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = AssignCustomerOfferingResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = AssignCustomerOfferingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AssignCustomerOfferingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AssignCustomerOfferingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AssignCustomerOfferingResponse400
    | AssignCustomerOfferingResponse401
    | AssignCustomerOfferingResponse403
    | AssignCustomerOfferingResponse404
    | AssignCustomerOfferingResponse409
    | AssignCustomerOfferingResponse422
    | AssignCustomerOfferingResponse423
    | AssignCustomerOfferingResponse429
    | AssignCustomerOfferingResponse500
    | AssignCustomerOfferingResponse503
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
    body: AssignCustomerOfferingBody,
) -> Response[
    Any
    | AssignCustomerOfferingResponse400
    | AssignCustomerOfferingResponse401
    | AssignCustomerOfferingResponse403
    | AssignCustomerOfferingResponse404
    | AssignCustomerOfferingResponse409
    | AssignCustomerOfferingResponse422
    | AssignCustomerOfferingResponse423
    | AssignCustomerOfferingResponse429
    | AssignCustomerOfferingResponse500
    | AssignCustomerOfferingResponse503
]:
    """Assign or clear an offering override for a customer

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>,
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (AssignCustomerOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssignCustomerOfferingResponse400 | AssignCustomerOfferingResponse401 | AssignCustomerOfferingResponse403 | AssignCustomerOfferingResponse404 | AssignCustomerOfferingResponse409 | AssignCustomerOfferingResponse422 | AssignCustomerOfferingResponse423 | AssignCustomerOfferingResponse429 | AssignCustomerOfferingResponse500 | AssignCustomerOfferingResponse503]
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
    body: AssignCustomerOfferingBody,
) -> (
    Any
    | AssignCustomerOfferingResponse400
    | AssignCustomerOfferingResponse401
    | AssignCustomerOfferingResponse403
    | AssignCustomerOfferingResponse404
    | AssignCustomerOfferingResponse409
    | AssignCustomerOfferingResponse422
    | AssignCustomerOfferingResponse423
    | AssignCustomerOfferingResponse429
    | AssignCustomerOfferingResponse500
    | AssignCustomerOfferingResponse503
    | None
):
    """Assign or clear an offering override for a customer

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>,
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (AssignCustomerOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssignCustomerOfferingResponse400 | AssignCustomerOfferingResponse401 | AssignCustomerOfferingResponse403 | AssignCustomerOfferingResponse404 | AssignCustomerOfferingResponse409 | AssignCustomerOfferingResponse422 | AssignCustomerOfferingResponse423 | AssignCustomerOfferingResponse429 | AssignCustomerOfferingResponse500 | AssignCustomerOfferingResponse503
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
    body: AssignCustomerOfferingBody,
) -> Response[
    Any
    | AssignCustomerOfferingResponse400
    | AssignCustomerOfferingResponse401
    | AssignCustomerOfferingResponse403
    | AssignCustomerOfferingResponse404
    | AssignCustomerOfferingResponse409
    | AssignCustomerOfferingResponse422
    | AssignCustomerOfferingResponse423
    | AssignCustomerOfferingResponse429
    | AssignCustomerOfferingResponse500
    | AssignCustomerOfferingResponse503
]:
    """Assign or clear an offering override for a customer

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>,
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (AssignCustomerOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssignCustomerOfferingResponse400 | AssignCustomerOfferingResponse401 | AssignCustomerOfferingResponse403 | AssignCustomerOfferingResponse404 | AssignCustomerOfferingResponse409 | AssignCustomerOfferingResponse422 | AssignCustomerOfferingResponse423 | AssignCustomerOfferingResponse429 | AssignCustomerOfferingResponse500 | AssignCustomerOfferingResponse503]
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
    body: AssignCustomerOfferingBody,
) -> (
    Any
    | AssignCustomerOfferingResponse400
    | AssignCustomerOfferingResponse401
    | AssignCustomerOfferingResponse403
    | AssignCustomerOfferingResponse404
    | AssignCustomerOfferingResponse409
    | AssignCustomerOfferingResponse422
    | AssignCustomerOfferingResponse423
    | AssignCustomerOfferingResponse429
    | AssignCustomerOfferingResponse500
    | AssignCustomerOfferingResponse503
    | None
):
    """Assign or clear an offering override for a customer

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>,
    <code>customer_information:customers:read_write</code>. This endpoint belongs to the
    <strong>Customer Information</strong> domain, which has a default rate limit of <strong>480 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        body (AssignCustomerOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssignCustomerOfferingResponse400 | AssignCustomerOfferingResponse401 | AssignCustomerOfferingResponse403 | AssignCustomerOfferingResponse404 | AssignCustomerOfferingResponse409 | AssignCustomerOfferingResponse422 | AssignCustomerOfferingResponse423 | AssignCustomerOfferingResponse429 | AssignCustomerOfferingResponse500 | AssignCustomerOfferingResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            customer_id=customer_id,
            client=client,
            body=body,
        )
    ).parsed
