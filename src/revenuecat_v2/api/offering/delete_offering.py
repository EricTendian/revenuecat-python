from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_offering_response_400 import DeleteOfferingResponse400
from ...models.delete_offering_response_401 import DeleteOfferingResponse401
from ...models.delete_offering_response_403 import DeleteOfferingResponse403
from ...models.delete_offering_response_404 import DeleteOfferingResponse404
from ...models.delete_offering_response_409 import DeleteOfferingResponse409
from ...models.delete_offering_response_422 import DeleteOfferingResponse422
from ...models.delete_offering_response_423 import DeleteOfferingResponse423
from ...models.delete_offering_response_429 import DeleteOfferingResponse429
from ...models.delete_offering_response_500 import DeleteOfferingResponse500
from ...models.delete_offering_response_503 import DeleteOfferingResponse503
from ...models.deleted_object import DeletedObject
from ...types import Response


def _get_kwargs(
    project_id: str,
    offering_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/offerings/{offering_id}".format(
            project_id=quote(str(project_id), safe=""),
            offering_id=quote(str(offering_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteOfferingResponse400
    | DeleteOfferingResponse401
    | DeleteOfferingResponse403
    | DeleteOfferingResponse404
    | DeleteOfferingResponse409
    | DeleteOfferingResponse422
    | DeleteOfferingResponse423
    | DeleteOfferingResponse429
    | DeleteOfferingResponse500
    | DeleteOfferingResponse503
    | DeletedObject
    | None
):
    if response.status_code == 200:
        response_200 = DeletedObject.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteOfferingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteOfferingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteOfferingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteOfferingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeleteOfferingResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = DeleteOfferingResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = DeleteOfferingResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = DeleteOfferingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteOfferingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteOfferingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteOfferingResponse400
    | DeleteOfferingResponse401
    | DeleteOfferingResponse403
    | DeleteOfferingResponse404
    | DeleteOfferingResponse409
    | DeleteOfferingResponse422
    | DeleteOfferingResponse423
    | DeleteOfferingResponse429
    | DeleteOfferingResponse500
    | DeleteOfferingResponse503
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
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteOfferingResponse400
    | DeleteOfferingResponse401
    | DeleteOfferingResponse403
    | DeleteOfferingResponse404
    | DeleteOfferingResponse409
    | DeleteOfferingResponse422
    | DeleteOfferingResponse423
    | DeleteOfferingResponse429
    | DeleteOfferingResponse500
    | DeleteOfferingResponse503
    | DeletedObject
]:
    """Delete an offering and its attached packages

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOfferingResponse400 | DeleteOfferingResponse401 | DeleteOfferingResponse403 | DeleteOfferingResponse404 | DeleteOfferingResponse409 | DeleteOfferingResponse422 | DeleteOfferingResponse423 | DeleteOfferingResponse429 | DeleteOfferingResponse500 | DeleteOfferingResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offering_id=offering_id,
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
) -> (
    DeleteOfferingResponse400
    | DeleteOfferingResponse401
    | DeleteOfferingResponse403
    | DeleteOfferingResponse404
    | DeleteOfferingResponse409
    | DeleteOfferingResponse422
    | DeleteOfferingResponse423
    | DeleteOfferingResponse429
    | DeleteOfferingResponse500
    | DeleteOfferingResponse503
    | DeletedObject
    | None
):
    """Delete an offering and its attached packages

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOfferingResponse400 | DeleteOfferingResponse401 | DeleteOfferingResponse403 | DeleteOfferingResponse404 | DeleteOfferingResponse409 | DeleteOfferingResponse422 | DeleteOfferingResponse423 | DeleteOfferingResponse429 | DeleteOfferingResponse500 | DeleteOfferingResponse503 | DeletedObject
    """

    return sync_detailed(
        project_id=project_id,
        offering_id=offering_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteOfferingResponse400
    | DeleteOfferingResponse401
    | DeleteOfferingResponse403
    | DeleteOfferingResponse404
    | DeleteOfferingResponse409
    | DeleteOfferingResponse422
    | DeleteOfferingResponse423
    | DeleteOfferingResponse429
    | DeleteOfferingResponse500
    | DeleteOfferingResponse503
    | DeletedObject
]:
    """Delete an offering and its attached packages

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOfferingResponse400 | DeleteOfferingResponse401 | DeleteOfferingResponse403 | DeleteOfferingResponse404 | DeleteOfferingResponse409 | DeleteOfferingResponse422 | DeleteOfferingResponse423 | DeleteOfferingResponse429 | DeleteOfferingResponse500 | DeleteOfferingResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offering_id=offering_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    offering_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteOfferingResponse400
    | DeleteOfferingResponse401
    | DeleteOfferingResponse403
    | DeleteOfferingResponse404
    | DeleteOfferingResponse409
    | DeleteOfferingResponse422
    | DeleteOfferingResponse423
    | DeleteOfferingResponse429
    | DeleteOfferingResponse500
    | DeleteOfferingResponse503
    | DeletedObject
    | None
):
    """Delete an offering and its attached packages

     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        offering_id (str):  Example: ofrnge1a2b3c4d5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOfferingResponse400 | DeleteOfferingResponse401 | DeleteOfferingResponse403 | DeleteOfferingResponse404 | DeleteOfferingResponse409 | DeleteOfferingResponse422 | DeleteOfferingResponse423 | DeleteOfferingResponse429 | DeleteOfferingResponse500 | DeleteOfferingResponse503 | DeletedObject
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            offering_id=offering_id,
            client=client,
        )
    ).parsed
