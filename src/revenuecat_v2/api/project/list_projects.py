from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_projects_response_400 import ListProjectsResponse400
from ...models.list_projects_response_401 import ListProjectsResponse401
from ...models.list_projects_response_403 import ListProjectsResponse403
from ...models.list_projects_response_404 import ListProjectsResponse404
from ...models.list_projects_response_423 import ListProjectsResponse423
from ...models.list_projects_response_429 import ListProjectsResponse429
from ...models.list_projects_response_500 import ListProjectsResponse500
from ...models.list_projects_response_503 import ListProjectsResponse503
from ...models.project_list import ProjectList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["starting_after"] = starting_after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListProjectsResponse400
    | ListProjectsResponse401
    | ListProjectsResponse403
    | ListProjectsResponse404
    | ListProjectsResponse423
    | ListProjectsResponse429
    | ListProjectsResponse500
    | ListProjectsResponse503
    | ProjectList
    | None
):
    if response.status_code == 200:
        response_200 = ProjectList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListProjectsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListProjectsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListProjectsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListProjectsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListProjectsResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListProjectsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListProjectsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListProjectsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListProjectsResponse400
    | ListProjectsResponse401
    | ListProjectsResponse403
    | ListProjectsResponse404
    | ListProjectsResponse423
    | ListProjectsResponse429
    | ListProjectsResponse500
    | ListProjectsResponse503
    | ProjectList
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    ListProjectsResponse400
    | ListProjectsResponse401
    | ListProjectsResponse403
    | ListProjectsResponse404
    | ListProjectsResponse423
    | ListProjectsResponse429
    | ListProjectsResponse500
    | ListProjectsResponse503
    | ProjectList
]:
    """Get a list of projects

     This endpoint requires the following permission(s):
    <code>project_configuration:projects:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProjectsResponse400 | ListProjectsResponse401 | ListProjectsResponse403 | ListProjectsResponse404 | ListProjectsResponse423 | ListProjectsResponse429 | ListProjectsResponse500 | ListProjectsResponse503 | ProjectList]
    """

    kwargs = _get_kwargs(
        starting_after=starting_after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    ListProjectsResponse400
    | ListProjectsResponse401
    | ListProjectsResponse403
    | ListProjectsResponse404
    | ListProjectsResponse423
    | ListProjectsResponse429
    | ListProjectsResponse500
    | ListProjectsResponse503
    | ProjectList
    | None
):
    """Get a list of projects

     This endpoint requires the following permission(s):
    <code>project_configuration:projects:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListProjectsResponse400 | ListProjectsResponse401 | ListProjectsResponse403 | ListProjectsResponse404 | ListProjectsResponse423 | ListProjectsResponse429 | ListProjectsResponse500 | ListProjectsResponse503 | ProjectList
    """

    return sync_detailed(
        client=client,
        starting_after=starting_after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    ListProjectsResponse400
    | ListProjectsResponse401
    | ListProjectsResponse403
    | ListProjectsResponse404
    | ListProjectsResponse423
    | ListProjectsResponse429
    | ListProjectsResponse500
    | ListProjectsResponse503
    | ProjectList
]:
    """Get a list of projects

     This endpoint requires the following permission(s):
    <code>project_configuration:projects:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProjectsResponse400 | ListProjectsResponse401 | ListProjectsResponse403 | ListProjectsResponse404 | ListProjectsResponse423 | ListProjectsResponse429 | ListProjectsResponse500 | ListProjectsResponse503 | ProjectList]
    """

    kwargs = _get_kwargs(
        starting_after=starting_after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    ListProjectsResponse400
    | ListProjectsResponse401
    | ListProjectsResponse403
    | ListProjectsResponse404
    | ListProjectsResponse423
    | ListProjectsResponse429
    | ListProjectsResponse500
    | ListProjectsResponse503
    | ProjectList
    | None
):
    """Get a list of projects

     This endpoint requires the following permission(s):
    <code>project_configuration:projects:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListProjectsResponse400 | ListProjectsResponse401 | ListProjectsResponse403 | ListProjectsResponse404 | ListProjectsResponse423 | ListProjectsResponse429 | ListProjectsResponse500 | ListProjectsResponse503 | ProjectList
    """

    return (
        await asyncio_detailed(
            client=client,
            starting_after=starting_after,
            limit=limit,
        )
    ).parsed
