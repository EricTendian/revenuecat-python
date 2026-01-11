from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_package_expand_item import GetPackageExpandItem
from ...models.get_package_response_400 import GetPackageResponse400
from ...models.get_package_response_401 import GetPackageResponse401
from ...models.get_package_response_403 import GetPackageResponse403
from ...models.get_package_response_404 import GetPackageResponse404
from ...models.get_package_response_423 import GetPackageResponse423
from ...models.get_package_response_429 import GetPackageResponse429
from ...models.get_package_response_500 import GetPackageResponse500
from ...models.get_package_response_503 import GetPackageResponse503
from ...models.package import Package
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    package_id: str,
    *,
    expand: list[GetPackageExpandItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_expand: list[str] | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item = expand_item_data.value
            json_expand.append(expand_item)

    params["expand"] = json_expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/packages/{package_id}".format(
            project_id=quote(str(project_id), safe=""),
            package_id=quote(str(package_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetPackageResponse400
    | GetPackageResponse401
    | GetPackageResponse403
    | GetPackageResponse404
    | GetPackageResponse423
    | GetPackageResponse429
    | GetPackageResponse500
    | GetPackageResponse503
    | Package
    | None
):
    if response.status_code == 200:
        response_200 = Package.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetPackageResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetPackageResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetPackageResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetPackageResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetPackageResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetPackageResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetPackageResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetPackageResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetPackageResponse400
    | GetPackageResponse401
    | GetPackageResponse403
    | GetPackageResponse404
    | GetPackageResponse423
    | GetPackageResponse429
    | GetPackageResponse500
    | GetPackageResponse503
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
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetPackageExpandItem] | Unset = UNSET,
) -> Response[
    GetPackageResponse400
    | GetPackageResponse401
    | GetPackageResponse403
    | GetPackageResponse404
    | GetPackageResponse423
    | GetPackageResponse429
    | GetPackageResponse500
    | GetPackageResponse503
    | Package
]:
    """Get a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        expand (list[GetPackageExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPackageResponse400 | GetPackageResponse401 | GetPackageResponse403 | GetPackageResponse404 | GetPackageResponse423 | GetPackageResponse429 | GetPackageResponse500 | GetPackageResponse503 | Package]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        package_id=package_id,
        expand=expand,
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
    expand: list[GetPackageExpandItem] | Unset = UNSET,
) -> (
    GetPackageResponse400
    | GetPackageResponse401
    | GetPackageResponse403
    | GetPackageResponse404
    | GetPackageResponse423
    | GetPackageResponse429
    | GetPackageResponse500
    | GetPackageResponse503
    | Package
    | None
):
    """Get a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        expand (list[GetPackageExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPackageResponse400 | GetPackageResponse401 | GetPackageResponse403 | GetPackageResponse404 | GetPackageResponse423 | GetPackageResponse429 | GetPackageResponse500 | GetPackageResponse503 | Package
    """

    return sync_detailed(
        project_id=project_id,
        package_id=package_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetPackageExpandItem] | Unset = UNSET,
) -> Response[
    GetPackageResponse400
    | GetPackageResponse401
    | GetPackageResponse403
    | GetPackageResponse404
    | GetPackageResponse423
    | GetPackageResponse429
    | GetPackageResponse500
    | GetPackageResponse503
    | Package
]:
    """Get a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        expand (list[GetPackageExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPackageResponse400 | GetPackageResponse401 | GetPackageResponse403 | GetPackageResponse404 | GetPackageResponse423 | GetPackageResponse429 | GetPackageResponse500 | GetPackageResponse503 | Package]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        package_id=package_id,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetPackageExpandItem] | Unset = UNSET,
) -> (
    GetPackageResponse400
    | GetPackageResponse401
    | GetPackageResponse403
    | GetPackageResponse404
    | GetPackageResponse423
    | GetPackageResponse429
    | GetPackageResponse500
    | GetPackageResponse503
    | Package
    | None
):
    """Get a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        expand (list[GetPackageExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPackageResponse400 | GetPackageResponse401 | GetPackageResponse403 | GetPackageResponse404 | GetPackageResponse423 | GetPackageResponse429 | GetPackageResponse500 | GetPackageResponse503 | Package
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            package_id=package_id,
            client=client,
            expand=expand,
        )
    ).parsed
