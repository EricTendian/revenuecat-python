from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_offerings_expand_item import ListOfferingsExpandItem
from ...models.list_offerings_response_400 import ListOfferingsResponse400
from ...models.list_offerings_response_401 import ListOfferingsResponse401
from ...models.list_offerings_response_403 import ListOfferingsResponse403
from ...models.list_offerings_response_404 import ListOfferingsResponse404
from ...models.list_offerings_response_423 import ListOfferingsResponse423
from ...models.list_offerings_response_429 import ListOfferingsResponse429
from ...models.list_offerings_response_500 import ListOfferingsResponse500
from ...models.list_offerings_response_503 import ListOfferingsResponse503
from ...models.offering_list import OfferingList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    starting_after: str | Unset = UNSET,
    limit: int | Unset = 20,
    expand: list[ListOfferingsExpandItem] | Unset = UNSET,
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
        "url": "/projects/{project_id}/offerings".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListOfferingsResponse400
    | ListOfferingsResponse401
    | ListOfferingsResponse403
    | ListOfferingsResponse404
    | ListOfferingsResponse423
    | ListOfferingsResponse429
    | ListOfferingsResponse500
    | ListOfferingsResponse503
    | OfferingList
    | None
):
    if response.status_code == 200:
        response_200 = OfferingList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListOfferingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListOfferingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListOfferingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListOfferingsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListOfferingsResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListOfferingsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListOfferingsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListOfferingsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListOfferingsResponse400
    | ListOfferingsResponse401
    | ListOfferingsResponse403
    | ListOfferingsResponse404
    | ListOfferingsResponse423
    | ListOfferingsResponse429
    | ListOfferingsResponse500
    | ListOfferingsResponse503
    | OfferingList
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
    expand: list[ListOfferingsExpandItem] | Unset = UNSET,
) -> Response[
    ListOfferingsResponse400
    | ListOfferingsResponse401
    | ListOfferingsResponse403
    | ListOfferingsResponse404
    | ListOfferingsResponse423
    | ListOfferingsResponse429
    | ListOfferingsResponse500
    | ListOfferingsResponse503
    | OfferingList
]:
    """Get a list of offerings

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListOfferingsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListOfferingsResponse400 | ListOfferingsResponse401 | ListOfferingsResponse403 | ListOfferingsResponse404 | ListOfferingsResponse423 | ListOfferingsResponse429 | ListOfferingsResponse500 | ListOfferingsResponse503 | OfferingList]
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
    expand: list[ListOfferingsExpandItem] | Unset = UNSET,
) -> (
    ListOfferingsResponse400
    | ListOfferingsResponse401
    | ListOfferingsResponse403
    | ListOfferingsResponse404
    | ListOfferingsResponse423
    | ListOfferingsResponse429
    | ListOfferingsResponse500
    | ListOfferingsResponse503
    | OfferingList
    | None
):
    """Get a list of offerings

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListOfferingsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListOfferingsResponse400 | ListOfferingsResponse401 | ListOfferingsResponse403 | ListOfferingsResponse404 | ListOfferingsResponse423 | ListOfferingsResponse429 | ListOfferingsResponse500 | ListOfferingsResponse503 | OfferingList
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
    expand: list[ListOfferingsExpandItem] | Unset = UNSET,
) -> Response[
    ListOfferingsResponse400
    | ListOfferingsResponse401
    | ListOfferingsResponse403
    | ListOfferingsResponse404
    | ListOfferingsResponse423
    | ListOfferingsResponse429
    | ListOfferingsResponse500
    | ListOfferingsResponse503
    | OfferingList
]:
    """Get a list of offerings

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListOfferingsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListOfferingsResponse400 | ListOfferingsResponse401 | ListOfferingsResponse403 | ListOfferingsResponse404 | ListOfferingsResponse423 | ListOfferingsResponse429 | ListOfferingsResponse500 | ListOfferingsResponse503 | OfferingList]
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
    expand: list[ListOfferingsExpandItem] | Unset = UNSET,
) -> (
    ListOfferingsResponse400
    | ListOfferingsResponse401
    | ListOfferingsResponse403
    | ListOfferingsResponse404
    | ListOfferingsResponse423
    | ListOfferingsResponse429
    | ListOfferingsResponse500
    | ListOfferingsResponse503
    | OfferingList
    | None
):
    """Get a list of offerings

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (str | Unset):  Example: ent12354.
        limit (int | Unset):  Default: 20. Example: 10.
        expand (list[ListOfferingsExpandItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListOfferingsResponse400 | ListOfferingsResponse401 | ListOfferingsResponse403 | ListOfferingsResponse404 | ListOfferingsResponse423 | ListOfferingsResponse429 | ListOfferingsResponse500 | ListOfferingsResponse503 | OfferingList
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
