from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app import App
from ...models.get_app_response_400 import GetAppResponse400
from ...models.get_app_response_401 import GetAppResponse401
from ...models.get_app_response_403 import GetAppResponse403
from ...models.get_app_response_404 import GetAppResponse404
from ...models.get_app_response_423 import GetAppResponse423
from ...models.get_app_response_429 import GetAppResponse429
from ...models.get_app_response_500 import GetAppResponse500
from ...models.get_app_response_503 import GetAppResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    app_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/apps/{app_id}".format(
            project_id=quote(str(project_id), safe=""),
            app_id=quote(str(app_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    App
    | GetAppResponse400
    | GetAppResponse401
    | GetAppResponse403
    | GetAppResponse404
    | GetAppResponse423
    | GetAppResponse429
    | GetAppResponse500
    | GetAppResponse503
    | None
):
    if response.status_code == 200:
        response_200 = App.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAppResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetAppResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetAppResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAppResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetAppResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetAppResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetAppResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetAppResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    App
    | GetAppResponse400
    | GetAppResponse401
    | GetAppResponse403
    | GetAppResponse404
    | GetAppResponse423
    | GetAppResponse429
    | GetAppResponse500
    | GetAppResponse503
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
    App
    | GetAppResponse400
    | GetAppResponse401
    | GetAppResponse403
    | GetAppResponse404
    | GetAppResponse423
    | GetAppResponse429
    | GetAppResponse500
    | GetAppResponse503
]:
    """Get an app

     This endpoint requires the following permission(s): <code>project_configuration:apps:read</code>.
    This endpoint belongs to the <strong>Project Configuration</strong> domain, which has a default rate
    limit of <strong>60 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[App | GetAppResponse400 | GetAppResponse401 | GetAppResponse403 | GetAppResponse404 | GetAppResponse423 | GetAppResponse429 | GetAppResponse500 | GetAppResponse503]
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
    App
    | GetAppResponse400
    | GetAppResponse401
    | GetAppResponse403
    | GetAppResponse404
    | GetAppResponse423
    | GetAppResponse429
    | GetAppResponse500
    | GetAppResponse503
    | None
):
    """Get an app

     This endpoint requires the following permission(s): <code>project_configuration:apps:read</code>.
    This endpoint belongs to the <strong>Project Configuration</strong> domain, which has a default rate
    limit of <strong>60 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        App | GetAppResponse400 | GetAppResponse401 | GetAppResponse403 | GetAppResponse404 | GetAppResponse423 | GetAppResponse429 | GetAppResponse500 | GetAppResponse503
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
    App
    | GetAppResponse400
    | GetAppResponse401
    | GetAppResponse403
    | GetAppResponse404
    | GetAppResponse423
    | GetAppResponse429
    | GetAppResponse500
    | GetAppResponse503
]:
    """Get an app

     This endpoint requires the following permission(s): <code>project_configuration:apps:read</code>.
    This endpoint belongs to the <strong>Project Configuration</strong> domain, which has a default rate
    limit of <strong>60 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[App | GetAppResponse400 | GetAppResponse401 | GetAppResponse403 | GetAppResponse404 | GetAppResponse423 | GetAppResponse429 | GetAppResponse500 | GetAppResponse503]
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
    App
    | GetAppResponse400
    | GetAppResponse401
    | GetAppResponse403
    | GetAppResponse404
    | GetAppResponse423
    | GetAppResponse429
    | GetAppResponse500
    | GetAppResponse503
    | None
):
    """Get an app

     This endpoint requires the following permission(s): <code>project_configuration:apps:read</code>.
    This endpoint belongs to the <strong>Project Configuration</strong> domain, which has a default rate
    limit of <strong>60 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        App | GetAppResponse400 | GetAppResponse401 | GetAppResponse403 | GetAppResponse404 | GetAppResponse423 | GetAppResponse429 | GetAppResponse500 | GetAppResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            app_id=app_id,
            client=client,
        )
    ).parsed
