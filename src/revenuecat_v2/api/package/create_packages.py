from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_packages_body import CreatePackagesBody
from ...models.create_packages_response_400 import CreatePackagesResponse400
from ...models.create_packages_response_401 import CreatePackagesResponse401
from ...models.create_packages_response_403 import CreatePackagesResponse403
from ...models.create_packages_response_404 import CreatePackagesResponse404
from ...models.create_packages_response_409 import CreatePackagesResponse409
from ...models.create_packages_response_422 import CreatePackagesResponse422
from ...models.create_packages_response_423 import CreatePackagesResponse423
from ...models.create_packages_response_429 import CreatePackagesResponse429
from ...models.create_packages_response_500 import CreatePackagesResponse500
from ...models.create_packages_response_503 import CreatePackagesResponse503
from ...models.package import Package
from ...types import Response


def _get_kwargs(
    project_id: str,
    offering_id: str,
    *,
    body: CreatePackagesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/offerings/{offering_id}/packages".format(
            project_id=quote(str(project_id), safe=""),
            offering_id=quote(str(offering_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreatePackagesResponse400
    | CreatePackagesResponse401
    | CreatePackagesResponse403
    | CreatePackagesResponse404
    | CreatePackagesResponse409
    | CreatePackagesResponse422
    | CreatePackagesResponse423
    | CreatePackagesResponse429
    | CreatePackagesResponse500
    | CreatePackagesResponse503
    | Package
    | None
):
    if response.status_code == 201:
        response_201 = Package.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreatePackagesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreatePackagesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreatePackagesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreatePackagesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreatePackagesResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CreatePackagesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = CreatePackagesResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = CreatePackagesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreatePackagesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreatePackagesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreatePackagesResponse400
    | CreatePackagesResponse401
    | CreatePackagesResponse403
    | CreatePackagesResponse404
    | CreatePackagesResponse409
    | CreatePackagesResponse422
    | CreatePackagesResponse423
    | CreatePackagesResponse429
    | CreatePackagesResponse500
    | CreatePackagesResponse503
    | Package
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePackagesBody,
) -> Response[
    CreatePackagesResponse400
    | CreatePackagesResponse401
    | CreatePackagesResponse403
    | CreatePackagesResponse404
    | CreatePackagesResponse409
    | CreatePackagesResponse422
    | CreatePackagesResponse423
    | CreatePackagesResponse429
    | CreatePackagesResponse500
    | CreatePackagesResponse503
    | Package
]:
    """Create a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        body (CreatePackagesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePackagesResponse400 | CreatePackagesResponse401 | CreatePackagesResponse403 | CreatePackagesResponse404 | CreatePackagesResponse409 | CreatePackagesResponse422 | CreatePackagesResponse423 | CreatePackagesResponse429 | CreatePackagesResponse500 | CreatePackagesResponse503 | Package]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offering_id=offering_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePackagesBody,
) -> (
    CreatePackagesResponse400
    | CreatePackagesResponse401
    | CreatePackagesResponse403
    | CreatePackagesResponse404
    | CreatePackagesResponse409
    | CreatePackagesResponse422
    | CreatePackagesResponse423
    | CreatePackagesResponse429
    | CreatePackagesResponse500
    | CreatePackagesResponse503
    | Package
    | None
):
    """Create a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        body (CreatePackagesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePackagesResponse400 | CreatePackagesResponse401 | CreatePackagesResponse403 | CreatePackagesResponse404 | CreatePackagesResponse409 | CreatePackagesResponse422 | CreatePackagesResponse423 | CreatePackagesResponse429 | CreatePackagesResponse500 | CreatePackagesResponse503 | Package
    """

    return sync_detailed(
        project_id=project_id,
        offering_id=offering_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePackagesBody,
) -> Response[
    CreatePackagesResponse400
    | CreatePackagesResponse401
    | CreatePackagesResponse403
    | CreatePackagesResponse404
    | CreatePackagesResponse409
    | CreatePackagesResponse422
    | CreatePackagesResponse423
    | CreatePackagesResponse429
    | CreatePackagesResponse500
    | CreatePackagesResponse503
    | Package
]:
    """Create a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        body (CreatePackagesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePackagesResponse400 | CreatePackagesResponse401 | CreatePackagesResponse403 | CreatePackagesResponse404 | CreatePackagesResponse409 | CreatePackagesResponse422 | CreatePackagesResponse423 | CreatePackagesResponse429 | CreatePackagesResponse500 | CreatePackagesResponse503 | Package]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offering_id=offering_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePackagesBody,
) -> (
    CreatePackagesResponse400
    | CreatePackagesResponse401
    | CreatePackagesResponse403
    | CreatePackagesResponse404
    | CreatePackagesResponse409
    | CreatePackagesResponse422
    | CreatePackagesResponse423
    | CreatePackagesResponse429
    | CreatePackagesResponse500
    | CreatePackagesResponse503
    | Package
    | None
):
    """Create a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        body (CreatePackagesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePackagesResponse400 | CreatePackagesResponse401 | CreatePackagesResponse403 | CreatePackagesResponse404 | CreatePackagesResponse409 | CreatePackagesResponse422 | CreatePackagesResponse423 | CreatePackagesResponse429 | CreatePackagesResponse500 | CreatePackagesResponse503 | Package
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            offering_id=offering_id,
            client=client,
            body=body,
        )
    ).parsed
