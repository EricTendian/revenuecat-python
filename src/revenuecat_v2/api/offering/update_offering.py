from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.offering import Offering
from ...models.update_offering_body import UpdateOfferingBody
from ...models.update_offering_response_400 import UpdateOfferingResponse400
from ...models.update_offering_response_401 import UpdateOfferingResponse401
from ...models.update_offering_response_403 import UpdateOfferingResponse403
from ...models.update_offering_response_404 import UpdateOfferingResponse404
from ...models.update_offering_response_409 import UpdateOfferingResponse409
from ...models.update_offering_response_422 import UpdateOfferingResponse422
from ...models.update_offering_response_423 import UpdateOfferingResponse423
from ...models.update_offering_response_429 import UpdateOfferingResponse429
from ...models.update_offering_response_500 import UpdateOfferingResponse500
from ...models.update_offering_response_503 import UpdateOfferingResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    offering_id: str,
    *,
    body: UpdateOfferingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/offerings/{offering_id}".format(
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
    Offering
    | UpdateOfferingResponse400
    | UpdateOfferingResponse401
    | UpdateOfferingResponse403
    | UpdateOfferingResponse404
    | UpdateOfferingResponse409
    | UpdateOfferingResponse422
    | UpdateOfferingResponse423
    | UpdateOfferingResponse429
    | UpdateOfferingResponse500
    | UpdateOfferingResponse503
    | None
):
    if response.status_code == 200:
        response_200 = Offering.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateOfferingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateOfferingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdateOfferingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateOfferingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdateOfferingResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = UpdateOfferingResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = UpdateOfferingResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = UpdateOfferingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateOfferingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateOfferingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Offering
    | UpdateOfferingResponse400
    | UpdateOfferingResponse401
    | UpdateOfferingResponse403
    | UpdateOfferingResponse404
    | UpdateOfferingResponse409
    | UpdateOfferingResponse422
    | UpdateOfferingResponse423
    | UpdateOfferingResponse429
    | UpdateOfferingResponse500
    | UpdateOfferingResponse503
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
    body: UpdateOfferingBody,
) -> Response[
    Offering
    | UpdateOfferingResponse400
    | UpdateOfferingResponse401
    | UpdateOfferingResponse403
    | UpdateOfferingResponse404
    | UpdateOfferingResponse409
    | UpdateOfferingResponse422
    | UpdateOfferingResponse423
    | UpdateOfferingResponse429
    | UpdateOfferingResponse500
    | UpdateOfferingResponse503
]:
    """Update an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        body (UpdateOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Offering | UpdateOfferingResponse400 | UpdateOfferingResponse401 | UpdateOfferingResponse403 | UpdateOfferingResponse404 | UpdateOfferingResponse409 | UpdateOfferingResponse422 | UpdateOfferingResponse423 | UpdateOfferingResponse429 | UpdateOfferingResponse500 | UpdateOfferingResponse503]
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
    body: UpdateOfferingBody,
) -> (
    Offering
    | UpdateOfferingResponse400
    | UpdateOfferingResponse401
    | UpdateOfferingResponse403
    | UpdateOfferingResponse404
    | UpdateOfferingResponse409
    | UpdateOfferingResponse422
    | UpdateOfferingResponse423
    | UpdateOfferingResponse429
    | UpdateOfferingResponse500
    | UpdateOfferingResponse503
    | None
):
    """Update an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        body (UpdateOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Offering | UpdateOfferingResponse400 | UpdateOfferingResponse401 | UpdateOfferingResponse403 | UpdateOfferingResponse404 | UpdateOfferingResponse409 | UpdateOfferingResponse422 | UpdateOfferingResponse423 | UpdateOfferingResponse429 | UpdateOfferingResponse500 | UpdateOfferingResponse503
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
    body: UpdateOfferingBody,
) -> Response[
    Offering
    | UpdateOfferingResponse400
    | UpdateOfferingResponse401
    | UpdateOfferingResponse403
    | UpdateOfferingResponse404
    | UpdateOfferingResponse409
    | UpdateOfferingResponse422
    | UpdateOfferingResponse423
    | UpdateOfferingResponse429
    | UpdateOfferingResponse500
    | UpdateOfferingResponse503
]:
    """Update an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        body (UpdateOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Offering | UpdateOfferingResponse400 | UpdateOfferingResponse401 | UpdateOfferingResponse403 | UpdateOfferingResponse404 | UpdateOfferingResponse409 | UpdateOfferingResponse422 | UpdateOfferingResponse423 | UpdateOfferingResponse429 | UpdateOfferingResponse500 | UpdateOfferingResponse503]
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
    body: UpdateOfferingBody,
) -> (
    Offering
    | UpdateOfferingResponse400
    | UpdateOfferingResponse401
    | UpdateOfferingResponse403
    | UpdateOfferingResponse404
    | UpdateOfferingResponse409
    | UpdateOfferingResponse422
    | UpdateOfferingResponse423
    | UpdateOfferingResponse429
    | UpdateOfferingResponse500
    | UpdateOfferingResponse503
    | None
):
    """Update an offering

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.
        body (UpdateOfferingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Offering | UpdateOfferingResponse400 | UpdateOfferingResponse401 | UpdateOfferingResponse403 | UpdateOfferingResponse404 | UpdateOfferingResponse409 | UpdateOfferingResponse422 | UpdateOfferingResponse423 | UpdateOfferingResponse429 | UpdateOfferingResponse500 | UpdateOfferingResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            offering_id=offering_id,
            client=client,
            body=body,
        )
    ).parsed
