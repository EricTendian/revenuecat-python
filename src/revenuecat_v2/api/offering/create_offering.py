from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_offering_body import CreateOfferingBody
from ...models.create_offering_response_400 import CreateOfferingResponse400
from ...models.create_offering_response_401 import CreateOfferingResponse401
from ...models.create_offering_response_403 import CreateOfferingResponse403
from ...models.create_offering_response_404 import CreateOfferingResponse404
from ...models.create_offering_response_409 import CreateOfferingResponse409
from ...models.create_offering_response_422 import CreateOfferingResponse422
from ...models.create_offering_response_423 import CreateOfferingResponse423
from ...models.create_offering_response_429 import CreateOfferingResponse429
from ...models.create_offering_response_500 import CreateOfferingResponse500
from ...models.create_offering_response_503 import CreateOfferingResponse503
from ...models.offering import Offering
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: CreateOfferingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/offerings".format(
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
    CreateOfferingResponse400
    | CreateOfferingResponse401
    | CreateOfferingResponse403
    | CreateOfferingResponse404
    | CreateOfferingResponse409
    | CreateOfferingResponse422
    | CreateOfferingResponse423
    | CreateOfferingResponse429
    | CreateOfferingResponse500
    | CreateOfferingResponse503
    | Offering
    | None
):
    if response.status_code == 201:
        response_201 = Offering.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateOfferingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateOfferingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreateOfferingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateOfferingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreateOfferingResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CreateOfferingResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = CreateOfferingResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = CreateOfferingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateOfferingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateOfferingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateOfferingResponse400
    | CreateOfferingResponse401
    | CreateOfferingResponse403
    | CreateOfferingResponse404
    | CreateOfferingResponse409
    | CreateOfferingResponse422
    | CreateOfferingResponse423
    | CreateOfferingResponse429
    | CreateOfferingResponse500
    | CreateOfferingResponse503
    | Offering
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
    body: CreateOfferingBody,
) -> Response[
    CreateOfferingResponse400
    | CreateOfferingResponse401
    | CreateOfferingResponse403
    | CreateOfferingResponse404
    | CreateOfferingResponse409
    | CreateOfferingResponse422
    | CreateOfferingResponse423
    | CreateOfferingResponse429
    | CreateOfferingResponse500
    | CreateOfferingResponse503
    | Offering
]:
    """Create an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOfferingResponse400 | CreateOfferingResponse401 | CreateOfferingResponse403 | CreateOfferingResponse404 | CreateOfferingResponse409 | CreateOfferingResponse422 | CreateOfferingResponse423 | CreateOfferingResponse429 | CreateOfferingResponse500 | CreateOfferingResponse503 | Offering]
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
    body: CreateOfferingBody,
) -> (
    CreateOfferingResponse400
    | CreateOfferingResponse401
    | CreateOfferingResponse403
    | CreateOfferingResponse404
    | CreateOfferingResponse409
    | CreateOfferingResponse422
    | CreateOfferingResponse423
    | CreateOfferingResponse429
    | CreateOfferingResponse500
    | CreateOfferingResponse503
    | Offering
    | None
):
    """Create an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOfferingResponse400 | CreateOfferingResponse401 | CreateOfferingResponse403 | CreateOfferingResponse404 | CreateOfferingResponse409 | CreateOfferingResponse422 | CreateOfferingResponse423 | CreateOfferingResponse429 | CreateOfferingResponse500 | CreateOfferingResponse503 | Offering
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
    body: CreateOfferingBody,
) -> Response[
    CreateOfferingResponse400
    | CreateOfferingResponse401
    | CreateOfferingResponse403
    | CreateOfferingResponse404
    | CreateOfferingResponse409
    | CreateOfferingResponse422
    | CreateOfferingResponse423
    | CreateOfferingResponse429
    | CreateOfferingResponse500
    | CreateOfferingResponse503
    | Offering
]:
    """Create an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOfferingResponse400 | CreateOfferingResponse401 | CreateOfferingResponse403 | CreateOfferingResponse404 | CreateOfferingResponse409 | CreateOfferingResponse422 | CreateOfferingResponse423 | CreateOfferingResponse429 | CreateOfferingResponse500 | CreateOfferingResponse503 | Offering]
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
    body: CreateOfferingBody,
) -> (
    CreateOfferingResponse400
    | CreateOfferingResponse401
    | CreateOfferingResponse403
    | CreateOfferingResponse404
    | CreateOfferingResponse409
    | CreateOfferingResponse422
    | CreateOfferingResponse423
    | CreateOfferingResponse429
    | CreateOfferingResponse500
    | CreateOfferingResponse503
    | Offering
    | None
):
    """Create an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOfferingResponse400 | CreateOfferingResponse401 | CreateOfferingResponse403 | CreateOfferingResponse404 | CreateOfferingResponse409 | CreateOfferingResponse422 | CreateOfferingResponse423 | CreateOfferingResponse429 | CreateOfferingResponse500 | CreateOfferingResponse503 | Offering
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
