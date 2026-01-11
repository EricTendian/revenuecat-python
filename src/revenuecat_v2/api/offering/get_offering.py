from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_offering_expand_item import GetOfferingExpandItem
from ...models.get_offering_response_400 import GetOfferingResponse400
from ...models.get_offering_response_401 import GetOfferingResponse401
from ...models.get_offering_response_403 import GetOfferingResponse403
from ...models.get_offering_response_404 import GetOfferingResponse404
from ...models.get_offering_response_423 import GetOfferingResponse423
from ...models.get_offering_response_429 import GetOfferingResponse429
from ...models.get_offering_response_500 import GetOfferingResponse500
from ...models.get_offering_response_503 import GetOfferingResponse503
from ...models.offering import Offering
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    offering_id: str,
    *,
    expand: list[GetOfferingExpandItem] | Unset = UNSET,
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
        "url": "/projects/{project_id}/offerings/{offering_id}".format(
            project_id=quote(str(project_id), safe=""),
            offering_id=quote(str(offering_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetOfferingResponse400
    | GetOfferingResponse401
    | GetOfferingResponse403
    | GetOfferingResponse404
    | GetOfferingResponse423
    | GetOfferingResponse429
    | GetOfferingResponse500
    | GetOfferingResponse503
    | Offering
    | None
):
    if response.status_code == 200:
        response_200 = Offering.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetOfferingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetOfferingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetOfferingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetOfferingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetOfferingResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetOfferingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetOfferingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetOfferingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetOfferingResponse400
    | GetOfferingResponse401
    | GetOfferingResponse403
    | GetOfferingResponse404
    | GetOfferingResponse423
    | GetOfferingResponse429
    | GetOfferingResponse500
    | GetOfferingResponse503
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
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetOfferingExpandItem] | Unset = UNSET,
) -> Response[
    GetOfferingResponse400
    | GetOfferingResponse401
    | GetOfferingResponse403
    | GetOfferingResponse404
    | GetOfferingResponse423
    | GetOfferingResponse429
    | GetOfferingResponse500
    | GetOfferingResponse503
    | Offering
]:
    """Get an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        expand (list[GetOfferingExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOfferingResponse400 | GetOfferingResponse401 | GetOfferingResponse403 | GetOfferingResponse404 | GetOfferingResponse423 | GetOfferingResponse429 | GetOfferingResponse500 | GetOfferingResponse503 | Offering]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offering_id=offering_id,
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
    expand: list[GetOfferingExpandItem] | Unset = UNSET,
) -> (
    GetOfferingResponse400
    | GetOfferingResponse401
    | GetOfferingResponse403
    | GetOfferingResponse404
    | GetOfferingResponse423
    | GetOfferingResponse429
    | GetOfferingResponse500
    | GetOfferingResponse503
    | Offering
    | None
):
    """Get an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        expand (list[GetOfferingExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOfferingResponse400 | GetOfferingResponse401 | GetOfferingResponse403 | GetOfferingResponse404 | GetOfferingResponse423 | GetOfferingResponse429 | GetOfferingResponse500 | GetOfferingResponse503 | Offering
    """

    return sync_detailed(
        project_id=project_id,
        offering_id=offering_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetOfferingExpandItem] | Unset = UNSET,
) -> Response[
    GetOfferingResponse400
    | GetOfferingResponse401
    | GetOfferingResponse403
    | GetOfferingResponse404
    | GetOfferingResponse423
    | GetOfferingResponse429
    | GetOfferingResponse500
    | GetOfferingResponse503
    | Offering
]:
    """Get an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        expand (list[GetOfferingExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOfferingResponse400 | GetOfferingResponse401 | GetOfferingResponse403 | GetOfferingResponse404 | GetOfferingResponse423 | GetOfferingResponse429 | GetOfferingResponse500 | GetOfferingResponse503 | Offering]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offering_id=offering_id,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: list[GetOfferingExpandItem] | Unset = UNSET,
) -> (
    GetOfferingResponse400
    | GetOfferingResponse401
    | GetOfferingResponse403
    | GetOfferingResponse404
    | GetOfferingResponse423
    | GetOfferingResponse429
    | GetOfferingResponse500
    | GetOfferingResponse503
    | Offering
    | None
):
    """Get an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        expand (list[GetOfferingExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOfferingResponse400 | GetOfferingResponse401 | GetOfferingResponse403 | GetOfferingResponse404 | GetOfferingResponse423 | GetOfferingResponse429 | GetOfferingResponse500 | GetOfferingResponse503 | Offering
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            offering_id=offering_id,
            client=client,
            expand=expand,
        )
    ).parsed
