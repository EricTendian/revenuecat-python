from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_app_response_400 import DeleteAppResponse400
from ...models.delete_app_response_401 import DeleteAppResponse401
from ...models.delete_app_response_403 import DeleteAppResponse403
from ...models.delete_app_response_404 import DeleteAppResponse404
from ...models.delete_app_response_409 import DeleteAppResponse409
from ...models.delete_app_response_422 import DeleteAppResponse422
from ...models.delete_app_response_423 import DeleteAppResponse423
from ...models.delete_app_response_429 import DeleteAppResponse429
from ...models.delete_app_response_500 import DeleteAppResponse500
from ...models.delete_app_response_503 import DeleteAppResponse503
from ...models.deleted_object import DeletedObject
from ...types import Response


def _get_kwargs(
    project_id: str,
    app_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/apps/{app_id}".format(
            project_id=quote(str(project_id), safe=""),
            app_id=quote(str(app_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteAppResponse400
    | DeleteAppResponse401
    | DeleteAppResponse403
    | DeleteAppResponse404
    | DeleteAppResponse409
    | DeleteAppResponse422
    | DeleteAppResponse423
    | DeleteAppResponse429
    | DeleteAppResponse500
    | DeleteAppResponse503
    | DeletedObject
    | None
):
    if response.status_code == 200:
        response_200 = DeletedObject.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteAppResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteAppResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteAppResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteAppResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeleteAppResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = DeleteAppResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = DeleteAppResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = DeleteAppResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteAppResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteAppResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteAppResponse400
    | DeleteAppResponse401
    | DeleteAppResponse403
    | DeleteAppResponse404
    | DeleteAppResponse409
    | DeleteAppResponse422
    | DeleteAppResponse423
    | DeleteAppResponse429
    | DeleteAppResponse500
    | DeleteAppResponse503
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
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteAppResponse400
    | DeleteAppResponse401
    | DeleteAppResponse403
    | DeleteAppResponse404
    | DeleteAppResponse409
    | DeleteAppResponse422
    | DeleteAppResponse423
    | DeleteAppResponse429
    | DeleteAppResponse500
    | DeleteAppResponse503
    | DeletedObject
]:
    """Delete an app

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAppResponse400 | DeleteAppResponse401 | DeleteAppResponse403 | DeleteAppResponse404 | DeleteAppResponse409 | DeleteAppResponse422 | DeleteAppResponse423 | DeleteAppResponse429 | DeleteAppResponse500 | DeleteAppResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        app_id=app_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteAppResponse400
    | DeleteAppResponse401
    | DeleteAppResponse403
    | DeleteAppResponse404
    | DeleteAppResponse409
    | DeleteAppResponse422
    | DeleteAppResponse423
    | DeleteAppResponse429
    | DeleteAppResponse500
    | DeleteAppResponse503
    | DeletedObject
    | None
):
    """Delete an app

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAppResponse400 | DeleteAppResponse401 | DeleteAppResponse403 | DeleteAppResponse404 | DeleteAppResponse409 | DeleteAppResponse422 | DeleteAppResponse423 | DeleteAppResponse429 | DeleteAppResponse500 | DeleteAppResponse503 | DeletedObject
    """

    return sync_detailed(
        project_id=project_id,
        app_id=app_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteAppResponse400
    | DeleteAppResponse401
    | DeleteAppResponse403
    | DeleteAppResponse404
    | DeleteAppResponse409
    | DeleteAppResponse422
    | DeleteAppResponse423
    | DeleteAppResponse429
    | DeleteAppResponse500
    | DeleteAppResponse503
    | DeletedObject
]:
    """Delete an app

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAppResponse400 | DeleteAppResponse401 | DeleteAppResponse403 | DeleteAppResponse404 | DeleteAppResponse409 | DeleteAppResponse422 | DeleteAppResponse423 | DeleteAppResponse429 | DeleteAppResponse500 | DeleteAppResponse503 | DeletedObject]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        app_id=app_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteAppResponse400
    | DeleteAppResponse401
    | DeleteAppResponse403
    | DeleteAppResponse404
    | DeleteAppResponse409
    | DeleteAppResponse422
    | DeleteAppResponse423
    | DeleteAppResponse429
    | DeleteAppResponse500
    | DeleteAppResponse503
    | DeletedObject
    | None
):
    """Delete an app

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAppResponse400 | DeleteAppResponse401 | DeleteAppResponse403 | DeleteAppResponse404 | DeleteAppResponse409 | DeleteAppResponse422 | DeleteAppResponse423 | DeleteAppResponse429 | DeleteAppResponse500 | DeleteAppResponse503 | DeletedObject
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            app_id=app_id,
            client=client,
        )
    ).parsed
