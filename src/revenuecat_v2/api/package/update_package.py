from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.package import Package
from ...models.update_package_body import UpdatePackageBody
from ...models.update_package_response_400 import UpdatePackageResponse400
from ...models.update_package_response_401 import UpdatePackageResponse401
from ...models.update_package_response_403 import UpdatePackageResponse403
from ...models.update_package_response_404 import UpdatePackageResponse404
from ...models.update_package_response_409 import UpdatePackageResponse409
from ...models.update_package_response_422 import UpdatePackageResponse422
from ...models.update_package_response_423 import UpdatePackageResponse423
from ...models.update_package_response_429 import UpdatePackageResponse429
from ...models.update_package_response_500 import UpdatePackageResponse500
from ...models.update_package_response_503 import UpdatePackageResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    package_id: str,
    *,
    body: UpdatePackageBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/packages/{package_id}".format(
            project_id=quote(str(project_id), safe=""),
            package_id=quote(str(package_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Package
    | UpdatePackageResponse400
    | UpdatePackageResponse401
    | UpdatePackageResponse403
    | UpdatePackageResponse404
    | UpdatePackageResponse409
    | UpdatePackageResponse422
    | UpdatePackageResponse423
    | UpdatePackageResponse429
    | UpdatePackageResponse500
    | UpdatePackageResponse503
    | None
):
    if response.status_code == 200:
        response_200 = Package.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdatePackageResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdatePackageResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdatePackageResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdatePackageResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdatePackageResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = UpdatePackageResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = UpdatePackageResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = UpdatePackageResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdatePackageResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdatePackageResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Package
    | UpdatePackageResponse400
    | UpdatePackageResponse401
    | UpdatePackageResponse403
    | UpdatePackageResponse404
    | UpdatePackageResponse409
    | UpdatePackageResponse422
    | UpdatePackageResponse423
    | UpdatePackageResponse429
    | UpdatePackageResponse500
    | UpdatePackageResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePackageBody,
) -> Response[
    Package
    | UpdatePackageResponse400
    | UpdatePackageResponse401
    | UpdatePackageResponse403
    | UpdatePackageResponse404
    | UpdatePackageResponse409
    | UpdatePackageResponse422
    | UpdatePackageResponse423
    | UpdatePackageResponse429
    | UpdatePackageResponse500
    | UpdatePackageResponse503
]:
    """Update a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (UpdatePackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Package | UpdatePackageResponse400 | UpdatePackageResponse401 | UpdatePackageResponse403 | UpdatePackageResponse404 | UpdatePackageResponse409 | UpdatePackageResponse422 | UpdatePackageResponse423 | UpdatePackageResponse429 | UpdatePackageResponse500 | UpdatePackageResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        package_id=package_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePackageBody,
) -> (
    Package
    | UpdatePackageResponse400
    | UpdatePackageResponse401
    | UpdatePackageResponse403
    | UpdatePackageResponse404
    | UpdatePackageResponse409
    | UpdatePackageResponse422
    | UpdatePackageResponse423
    | UpdatePackageResponse429
    | UpdatePackageResponse500
    | UpdatePackageResponse503
    | None
):
    """Update a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (UpdatePackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Package | UpdatePackageResponse400 | UpdatePackageResponse401 | UpdatePackageResponse403 | UpdatePackageResponse404 | UpdatePackageResponse409 | UpdatePackageResponse422 | UpdatePackageResponse423 | UpdatePackageResponse429 | UpdatePackageResponse500 | UpdatePackageResponse503
    """

    return sync_detailed(
        project_id=project_id,
        package_id=package_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePackageBody,
) -> Response[
    Package
    | UpdatePackageResponse400
    | UpdatePackageResponse401
    | UpdatePackageResponse403
    | UpdatePackageResponse404
    | UpdatePackageResponse409
    | UpdatePackageResponse422
    | UpdatePackageResponse423
    | UpdatePackageResponse429
    | UpdatePackageResponse500
    | UpdatePackageResponse503
]:
    """Update a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (UpdatePackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Package | UpdatePackageResponse400 | UpdatePackageResponse401 | UpdatePackageResponse403 | UpdatePackageResponse404 | UpdatePackageResponse409 | UpdatePackageResponse422 | UpdatePackageResponse423 | UpdatePackageResponse429 | UpdatePackageResponse500 | UpdatePackageResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        package_id=package_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePackageBody,
) -> (
    Package
    | UpdatePackageResponse400
    | UpdatePackageResponse401
    | UpdatePackageResponse403
    | UpdatePackageResponse404
    | UpdatePackageResponse409
    | UpdatePackageResponse422
    | UpdatePackageResponse423
    | UpdatePackageResponse429
    | UpdatePackageResponse500
    | UpdatePackageResponse503
    | None
):
    """Update a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (UpdatePackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Package | UpdatePackageResponse400 | UpdatePackageResponse401 | UpdatePackageResponse403 | UpdatePackageResponse404 | UpdatePackageResponse409 | UpdatePackageResponse422 | UpdatePackageResponse423 | UpdatePackageResponse429 | UpdatePackageResponse500 | UpdatePackageResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            package_id=package_id,
            client=client,
            body=body,
        )
    ).parsed
