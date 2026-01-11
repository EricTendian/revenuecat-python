from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_package_from_offering_response_400 import DeletePackageFromOfferingResponse400
from ...models.delete_package_from_offering_response_401 import DeletePackageFromOfferingResponse401
from ...models.delete_package_from_offering_response_403 import DeletePackageFromOfferingResponse403
from ...models.delete_package_from_offering_response_404 import DeletePackageFromOfferingResponse404
from ...models.delete_package_from_offering_response_409 import DeletePackageFromOfferingResponse409
from ...models.delete_package_from_offering_response_422 import DeletePackageFromOfferingResponse422
from ...models.delete_package_from_offering_response_423 import DeletePackageFromOfferingResponse423
from ...models.delete_package_from_offering_response_429 import DeletePackageFromOfferingResponse429
from ...models.delete_package_from_offering_response_500 import DeletePackageFromOfferingResponse500
from ...models.delete_package_from_offering_response_503 import DeletePackageFromOfferingResponse503
from ...models.deleted_object import DeletedObject
from ...types import Response


def _get_kwargs(
    project_id: str,
    package_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/packages/{package_id}".format(
            project_id=quote(str(project_id), safe=""),
            package_id=quote(str(package_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeletePackageFromOfferingResponse400
    | DeletePackageFromOfferingResponse401
    | DeletePackageFromOfferingResponse403
    | DeletePackageFromOfferingResponse404
    | DeletePackageFromOfferingResponse409
    | DeletePackageFromOfferingResponse422
    | DeletePackageFromOfferingResponse423
    | DeletePackageFromOfferingResponse429
    | DeletePackageFromOfferingResponse500
    | DeletePackageFromOfferingResponse503
    | DeletedObject
    | None
):
    if response.status_code == 200:
        response_200 = DeletedObject.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeletePackageFromOfferingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeletePackageFromOfferingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeletePackageFromOfferingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeletePackageFromOfferingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeletePackageFromOfferingResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = DeletePackageFromOfferingResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = DeletePackageFromOfferingResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = DeletePackageFromOfferingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeletePackageFromOfferingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeletePackageFromOfferingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeletePackageFromOfferingResponse400
    | DeletePackageFromOfferingResponse401
    | DeletePackageFromOfferingResponse403
    | DeletePackageFromOfferingResponse404
    | DeletePackageFromOfferingResponse409
    | DeletePackageFromOfferingResponse422
    | DeletePackageFromOfferingResponse423
    | DeletePackageFromOfferingResponse429
    | DeletePackageFromOfferingResponse500
    | DeletePackageFromOfferingResponse503
    | DeletedObject
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
) -> Response[
    DeletePackageFromOfferingResponse400
    | DeletePackageFromOfferingResponse401
    | DeletePackageFromOfferingResponse403
    | DeletePackageFromOfferingResponse404
    | DeletePackageFromOfferingResponse409
    | DeletePackageFromOfferingResponse422
    | DeletePackageFromOfferingResponse423
    | DeletePackageFromOfferingResponse429
    | DeletePackageFromOfferingResponse500
    | DeletePackageFromOfferingResponse503
    | DeletedObject
]:
    """Delete a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeletePackageFromOfferingResponse400 | DeletePackageFromOfferingResponse401 | DeletePackageFromOfferingResponse403 | DeletePackageFromOfferingResponse404 | DeletePackageFromOfferingResponse409 | DeletePackageFromOfferingResponse422 | DeletePackageFromOfferingResponse423 | DeletePackageFromOfferingResponse429 | DeletePackageFromOfferingResponse500 | DeletePackageFromOfferingResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        package_id=package_id,
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
) -> (
    DeletePackageFromOfferingResponse400
    | DeletePackageFromOfferingResponse401
    | DeletePackageFromOfferingResponse403
    | DeletePackageFromOfferingResponse404
    | DeletePackageFromOfferingResponse409
    | DeletePackageFromOfferingResponse422
    | DeletePackageFromOfferingResponse423
    | DeletePackageFromOfferingResponse429
    | DeletePackageFromOfferingResponse500
    | DeletePackageFromOfferingResponse503
    | DeletedObject
    | None
):
    """Delete a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeletePackageFromOfferingResponse400 | DeletePackageFromOfferingResponse401 | DeletePackageFromOfferingResponse403 | DeletePackageFromOfferingResponse404 | DeletePackageFromOfferingResponse409 | DeletePackageFromOfferingResponse422 | DeletePackageFromOfferingResponse423 | DeletePackageFromOfferingResponse429 | DeletePackageFromOfferingResponse500 | DeletePackageFromOfferingResponse503 | DeletedObject
    """

    return sync_detailed(
        project_id=project_id,
        package_id=package_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeletePackageFromOfferingResponse400
    | DeletePackageFromOfferingResponse401
    | DeletePackageFromOfferingResponse403
    | DeletePackageFromOfferingResponse404
    | DeletePackageFromOfferingResponse409
    | DeletePackageFromOfferingResponse422
    | DeletePackageFromOfferingResponse423
    | DeletePackageFromOfferingResponse429
    | DeletePackageFromOfferingResponse500
    | DeletePackageFromOfferingResponse503
    | DeletedObject
]:
    """Delete a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeletePackageFromOfferingResponse400 | DeletePackageFromOfferingResponse401 | DeletePackageFromOfferingResponse403 | DeletePackageFromOfferingResponse404 | DeletePackageFromOfferingResponse409 | DeletePackageFromOfferingResponse422 | DeletePackageFromOfferingResponse423 | DeletePackageFromOfferingResponse429 | DeletePackageFromOfferingResponse500 | DeletePackageFromOfferingResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        package_id=package_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeletePackageFromOfferingResponse400
    | DeletePackageFromOfferingResponse401
    | DeletePackageFromOfferingResponse403
    | DeletePackageFromOfferingResponse404
    | DeletePackageFromOfferingResponse409
    | DeletePackageFromOfferingResponse422
    | DeletePackageFromOfferingResponse423
    | DeletePackageFromOfferingResponse429
    | DeletePackageFromOfferingResponse500
    | DeletePackageFromOfferingResponse503
    | DeletedObject
    | None
):
    """Delete a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeletePackageFromOfferingResponse400 | DeletePackageFromOfferingResponse401 | DeletePackageFromOfferingResponse403 | DeletePackageFromOfferingResponse404 | DeletePackageFromOfferingResponse409 | DeletePackageFromOfferingResponse422 | DeletePackageFromOfferingResponse423 | DeletePackageFromOfferingResponse429 | DeletePackageFromOfferingResponse500 | DeletePackageFromOfferingResponse503 | DeletedObject
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            package_id=package_id,
            client=client,
        )
    ).parsed
