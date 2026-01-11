from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entitlement_list import EntitlementList
from ...models.list_entitlements_expand_item import ListEntitlementsExpandItem
from ...models.list_entitlements_response_400 import ListEntitlementsResponse400
from ...models.list_entitlements_response_401 import ListEntitlementsResponse401
from ...models.list_entitlements_response_403 import ListEntitlementsResponse403
from ...models.list_entitlements_response_404 import ListEntitlementsResponse404
from ...models.list_entitlements_response_423 import ListEntitlementsResponse423
from ...models.list_entitlements_response_429 import ListEntitlementsResponse429
from ...models.list_entitlements_response_500 import ListEntitlementsResponse500
from ...models.list_entitlements_response_503 import ListEntitlementsResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListEntitlementsExpandItem] | Unset = UNSET,
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
        "url": "/projects/{project_id}/entitlements".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EntitlementList
    | ListEntitlementsResponse400
    | ListEntitlementsResponse401
    | ListEntitlementsResponse403
    | ListEntitlementsResponse404
    | ListEntitlementsResponse423
    | ListEntitlementsResponse429
    | ListEntitlementsResponse500
    | ListEntitlementsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = EntitlementList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListEntitlementsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListEntitlementsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListEntitlementsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListEntitlementsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListEntitlementsResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListEntitlementsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListEntitlementsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListEntitlementsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EntitlementList
    | ListEntitlementsResponse400
    | ListEntitlementsResponse401
    | ListEntitlementsResponse403
    | ListEntitlementsResponse404
    | ListEntitlementsResponse423
    | ListEntitlementsResponse429
    | ListEntitlementsResponse500
    | ListEntitlementsResponse503
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
    expand: list[ListEntitlementsExpandItem] | Unset = UNSET,
) -> Response[
    EntitlementList
    | ListEntitlementsResponse400
    | ListEntitlementsResponse401
    | ListEntitlementsResponse403
    | ListEntitlementsResponse404
    | ListEntitlementsResponse423
    | ListEntitlementsResponse429
    | ListEntitlementsResponse500
    | ListEntitlementsResponse503
]:
    """Get a list of entitlements

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListEntitlementsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntitlementList | ListEntitlementsResponse400 | ListEntitlementsResponse401 | ListEntitlementsResponse403 | ListEntitlementsResponse404 | ListEntitlementsResponse423 | ListEntitlementsResponse429 | ListEntitlementsResponse500 | ListEntitlementsResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
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
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListEntitlementsExpandItem] | Unset = UNSET,
) -> (
    EntitlementList
    | ListEntitlementsResponse400
    | ListEntitlementsResponse401
    | ListEntitlementsResponse403
    | ListEntitlementsResponse404
    | ListEntitlementsResponse423
    | ListEntitlementsResponse429
    | ListEntitlementsResponse500
    | ListEntitlementsResponse503
    | None
):
    """Get a list of entitlements

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListEntitlementsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntitlementList | ListEntitlementsResponse400 | ListEntitlementsResponse401 | ListEntitlementsResponse403 | ListEntitlementsResponse404 | ListEntitlementsResponse423 | ListEntitlementsResponse429 | ListEntitlementsResponse500 | ListEntitlementsResponse503
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListEntitlementsExpandItem] | Unset = UNSET,
) -> Response[
    EntitlementList
    | ListEntitlementsResponse400
    | ListEntitlementsResponse401
    | ListEntitlementsResponse403
    | ListEntitlementsResponse404
    | ListEntitlementsResponse423
    | ListEntitlementsResponse429
    | ListEntitlementsResponse500
    | ListEntitlementsResponse503
]:
    """Get a list of entitlements

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListEntitlementsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntitlementList | ListEntitlementsResponse400 | ListEntitlementsResponse401 | ListEntitlementsResponse403 | ListEntitlementsResponse404 | ListEntitlementsResponse423 | ListEntitlementsResponse429 | ListEntitlementsResponse500 | ListEntitlementsResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListEntitlementsExpandItem] | Unset = UNSET,
) -> (
    EntitlementList
    | ListEntitlementsResponse400
    | ListEntitlementsResponse401
    | ListEntitlementsResponse403
    | ListEntitlementsResponse404
    | ListEntitlementsResponse423
    | ListEntitlementsResponse429
    | ListEntitlementsResponse500
    | ListEntitlementsResponse503
    | None
):
    """Get a list of entitlements

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListEntitlementsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntitlementList | ListEntitlementsResponse400 | ListEntitlementsResponse401 | ListEntitlementsResponse403 | ListEntitlementsResponse404 | ListEntitlementsResponse423 | ListEntitlementsResponse429 | ListEntitlementsResponse500 | ListEntitlementsResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            starting_after=starting_after,
            limit=limit,
            expand=expand,
        )
    ).parsed
