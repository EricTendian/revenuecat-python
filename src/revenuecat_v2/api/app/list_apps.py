from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_list import AppList
from ...models.list_apps_response_400 import ListAppsResponse400
from ...models.list_apps_response_401 import ListAppsResponse401
from ...models.list_apps_response_403 import ListAppsResponse403
from ...models.list_apps_response_404 import ListAppsResponse404
from ...models.list_apps_response_423 import ListAppsResponse423
from ...models.list_apps_response_429 import ListAppsResponse429
from ...models.list_apps_response_500 import ListAppsResponse500
from ...models.list_apps_response_503 import ListAppsResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
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
        "url": "/projects/{project_id}/apps".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AppList
    | ListAppsResponse400
    | ListAppsResponse401
    | ListAppsResponse403
    | ListAppsResponse404
    | ListAppsResponse423
    | ListAppsResponse429
    | ListAppsResponse500
    | ListAppsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AppList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListAppsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListAppsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListAppsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListAppsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListAppsResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListAppsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListAppsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListAppsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AppList
    | ListAppsResponse400
    | ListAppsResponse401
    | ListAppsResponse403
    | ListAppsResponse404
    | ListAppsResponse423
    | ListAppsResponse429
    | ListAppsResponse500
    | ListAppsResponse503
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
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    AppList
    | ListAppsResponse400
    | ListAppsResponse401
    | ListAppsResponse403
    | ListAppsResponse404
    | ListAppsResponse423
    | ListAppsResponse429
    | ListAppsResponse500
    | ListAppsResponse503
]:
    """Get a list of apps

     This endpoint requires the following permission(s): <code>project_configuration:apps:read</code>.
    This endpoint belongs to the <strong>Project Configuration</strong> domain, which has a default rate
    limit of <strong>60 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppList | ListAppsResponse400 | ListAppsResponse401 | ListAppsResponse403 | ListAppsResponse404 | ListAppsResponse423 | ListAppsResponse429 | ListAppsResponse500 | ListAppsResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        starting_after=starting_after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    AppList
    | ListAppsResponse400
    | ListAppsResponse401
    | ListAppsResponse403
    | ListAppsResponse404
    | ListAppsResponse423
    | ListAppsResponse429
    | ListAppsResponse500
    | ListAppsResponse503
    | None
):
    """Get a list of apps

     This endpoint requires the following permission(s): <code>project_configuration:apps:read</code>.
    This endpoint belongs to the <strong>Project Configuration</strong> domain, which has a default rate
    limit of <strong>60 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppList | ListAppsResponse400 | ListAppsResponse401 | ListAppsResponse403 | ListAppsResponse404 | ListAppsResponse423 | ListAppsResponse429 | ListAppsResponse500 | ListAppsResponse503
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        starting_after=starting_after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[
    AppList
    | ListAppsResponse400
    | ListAppsResponse401
    | ListAppsResponse403
    | ListAppsResponse404
    | ListAppsResponse423
    | ListAppsResponse429
    | ListAppsResponse500
    | ListAppsResponse503
]:
    """Get a list of apps

     This endpoint requires the following permission(s): <code>project_configuration:apps:read</code>.
    This endpoint belongs to the <strong>Project Configuration</strong> domain, which has a default rate
    limit of <strong>60 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppList | ListAppsResponse400 | ListAppsResponse401 | ListAppsResponse403 | ListAppsResponse404 | ListAppsResponse423 | ListAppsResponse429 | ListAppsResponse500 | ListAppsResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        starting_after=starting_after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> (
    AppList
    | ListAppsResponse400
    | ListAppsResponse401
    | ListAppsResponse403
    | ListAppsResponse404
    | ListAppsResponse423
    | ListAppsResponse429
    | ListAppsResponse500
    | ListAppsResponse503
    | None
):
    """Get a list of apps

     This endpoint requires the following permission(s): <code>project_configuration:apps:read</code>.
    This endpoint belongs to the <strong>Project Configuration</strong> domain, which has a default rate
    limit of <strong>60 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppList | ListAppsResponse400 | ListAppsResponse401 | ListAppsResponse403 | ListAppsResponse404 | ListAppsResponse423 | ListAppsResponse429 | ListAppsResponse500 | ListAppsResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            starting_after=starting_after,
            limit=limit,
        )
    ).parsed
