from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_packages_expand_item import ListPackagesExpandItem
from ...models.list_packages_response_400 import ListPackagesResponse400
from ...models.list_packages_response_401 import ListPackagesResponse401
from ...models.list_packages_response_403 import ListPackagesResponse403
from ...models.list_packages_response_404 import ListPackagesResponse404
from ...models.list_packages_response_423 import ListPackagesResponse423
from ...models.list_packages_response_429 import ListPackagesResponse429
from ...models.list_packages_response_500 import ListPackagesResponse500
from ...models.list_packages_response_503 import ListPackagesResponse503
from ...models.package_list import PackageList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    offering_id: str,
    *,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListPackagesExpandItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["starting_after"] = starting_after

    params["limit"] = limit

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
        "url": "/projects/{project_id}/offerings/{offering_id}/packages".format(
            project_id=quote(str(project_id), safe=""),
            offering_id=quote(str(offering_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListPackagesResponse400
    | ListPackagesResponse401
    | ListPackagesResponse403
    | ListPackagesResponse404
    | ListPackagesResponse423
    | ListPackagesResponse429
    | ListPackagesResponse500
    | ListPackagesResponse503
    | PackageList
    | None
):
    if response.status_code == 200:
        response_200 = PackageList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListPackagesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListPackagesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListPackagesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListPackagesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListPackagesResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListPackagesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListPackagesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListPackagesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListPackagesResponse400
    | ListPackagesResponse401
    | ListPackagesResponse403
    | ListPackagesResponse404
    | ListPackagesResponse423
    | ListPackagesResponse429
    | ListPackagesResponse500
    | ListPackagesResponse503
    | PackageList
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
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListPackagesExpandItem] | Unset = UNSET,
) -> Response[
    ListPackagesResponse400
    | ListPackagesResponse401
    | ListPackagesResponse403
    | ListPackagesResponse404
    | ListPackagesResponse423
    | ListPackagesResponse429
    | ListPackagesResponse500
    | ListPackagesResponse503
    | PackageList
]:
    """Get a list of packages in an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListPackagesExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPackagesResponse400 | ListPackagesResponse401 | ListPackagesResponse403 | ListPackagesResponse404 | ListPackagesResponse423 | ListPackagesResponse429 | ListPackagesResponse500 | ListPackagesResponse503 | PackageList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offering_id=offering_id,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
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
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListPackagesExpandItem] | Unset = UNSET,
) -> (
    ListPackagesResponse400
    | ListPackagesResponse401
    | ListPackagesResponse403
    | ListPackagesResponse404
    | ListPackagesResponse423
    | ListPackagesResponse429
    | ListPackagesResponse500
    | ListPackagesResponse503
    | PackageList
    | None
):
    """Get a list of packages in an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListPackagesExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPackagesResponse400 | ListPackagesResponse401 | ListPackagesResponse403 | ListPackagesResponse404 | ListPackagesResponse423 | ListPackagesResponse429 | ListPackagesResponse500 | ListPackagesResponse503 | PackageList
    """

    return sync_detailed(
        project_id=project_id,
        offering_id=offering_id,
        client=client,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListPackagesExpandItem] | Unset = UNSET,
) -> Response[
    ListPackagesResponse400
    | ListPackagesResponse401
    | ListPackagesResponse403
    | ListPackagesResponse404
    | ListPackagesResponse423
    | ListPackagesResponse429
    | ListPackagesResponse500
    | ListPackagesResponse503
    | PackageList
]:
    """Get a list of packages in an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListPackagesExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPackagesResponse400 | ListPackagesResponse401 | ListPackagesResponse403 | ListPackagesResponse404 | ListPackagesResponse423 | ListPackagesResponse429 | ListPackagesResponse500 | ListPackagesResponse503 | PackageList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offering_id=offering_id,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListPackagesExpandItem] | Unset = UNSET,
) -> (
    ListPackagesResponse400
    | ListPackagesResponse401
    | ListPackagesResponse403
    | ListPackagesResponse404
    | ListPackagesResponse423
    | ListPackagesResponse429
    | ListPackagesResponse500
    | ListPackagesResponse503
    | PackageList
    | None
):
    """Get a list of packages in an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListPackagesExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPackagesResponse400 | ListPackagesResponse401 | ListPackagesResponse403 | ListPackagesResponse404 | ListPackagesResponse423 | ListPackagesResponse429 | ListPackagesResponse500 | ListPackagesResponse503 | PackageList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            offering_id=offering_id,
            client=client,
            starting_after=starting_after,
            limit=limit,
            expand=expand,
        )
    ).parsed
