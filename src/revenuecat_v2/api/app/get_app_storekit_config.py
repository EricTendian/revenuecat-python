from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_app_storekit_config_response_400 import GetAppStorekitConfigResponse400
from ...models.get_app_storekit_config_response_401 import GetAppStorekitConfigResponse401
from ...models.get_app_storekit_config_response_403 import GetAppStorekitConfigResponse403
from ...models.get_app_storekit_config_response_404 import GetAppStorekitConfigResponse404
from ...models.get_app_storekit_config_response_423 import GetAppStorekitConfigResponse423
from ...models.get_app_storekit_config_response_429 import GetAppStorekitConfigResponse429
from ...models.get_app_storekit_config_response_500 import GetAppStorekitConfigResponse500
from ...models.get_app_storekit_config_response_503 import GetAppStorekitConfigResponse503
from ...models.store_kit_config_file import StoreKitConfigFile
from ...types import Response


def _get_kwargs(
    project_id: str,
    app_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/apps/{app_id}/store_kit_config".format(
            project_id=quote(str(project_id), safe=""),
            app_id=quote(str(app_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAppStorekitConfigResponse400
    | GetAppStorekitConfigResponse401
    | GetAppStorekitConfigResponse403
    | GetAppStorekitConfigResponse404
    | GetAppStorekitConfigResponse423
    | GetAppStorekitConfigResponse429
    | GetAppStorekitConfigResponse500
    | GetAppStorekitConfigResponse503
    | StoreKitConfigFile
    | None
):
    if response.status_code == 200:
        response_200 = StoreKitConfigFile.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAppStorekitConfigResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetAppStorekitConfigResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetAppStorekitConfigResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAppStorekitConfigResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetAppStorekitConfigResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetAppStorekitConfigResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetAppStorekitConfigResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetAppStorekitConfigResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAppStorekitConfigResponse400
    | GetAppStorekitConfigResponse401
    | GetAppStorekitConfigResponse403
    | GetAppStorekitConfigResponse404
    | GetAppStorekitConfigResponse423
    | GetAppStorekitConfigResponse429
    | GetAppStorekitConfigResponse500
    | GetAppStorekitConfigResponse503
    | StoreKitConfigFile
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
    GetAppStorekitConfigResponse400
    | GetAppStorekitConfigResponse401
    | GetAppStorekitConfigResponse403
    | GetAppStorekitConfigResponse404
    | GetAppStorekitConfigResponse423
    | GetAppStorekitConfigResponse429
    | GetAppStorekitConfigResponse500
    | GetAppStorekitConfigResponse503
    | StoreKitConfigFile
]:
    """Get the StoreKit configuration for an app

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
        Response[GetAppStorekitConfigResponse400 | GetAppStorekitConfigResponse401 | GetAppStorekitConfigResponse403 | GetAppStorekitConfigResponse404 | GetAppStorekitConfigResponse423 | GetAppStorekitConfigResponse429 | GetAppStorekitConfigResponse500 | GetAppStorekitConfigResponse503 | StoreKitConfigFile]
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
    GetAppStorekitConfigResponse400
    | GetAppStorekitConfigResponse401
    | GetAppStorekitConfigResponse403
    | GetAppStorekitConfigResponse404
    | GetAppStorekitConfigResponse423
    | GetAppStorekitConfigResponse429
    | GetAppStorekitConfigResponse500
    | GetAppStorekitConfigResponse503
    | StoreKitConfigFile
    | None
):
    """Get the StoreKit configuration for an app

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
        GetAppStorekitConfigResponse400 | GetAppStorekitConfigResponse401 | GetAppStorekitConfigResponse403 | GetAppStorekitConfigResponse404 | GetAppStorekitConfigResponse423 | GetAppStorekitConfigResponse429 | GetAppStorekitConfigResponse500 | GetAppStorekitConfigResponse503 | StoreKitConfigFile
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
    GetAppStorekitConfigResponse400
    | GetAppStorekitConfigResponse401
    | GetAppStorekitConfigResponse403
    | GetAppStorekitConfigResponse404
    | GetAppStorekitConfigResponse423
    | GetAppStorekitConfigResponse429
    | GetAppStorekitConfigResponse500
    | GetAppStorekitConfigResponse503
    | StoreKitConfigFile
]:
    """Get the StoreKit configuration for an app

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
        Response[GetAppStorekitConfigResponse400 | GetAppStorekitConfigResponse401 | GetAppStorekitConfigResponse403 | GetAppStorekitConfigResponse404 | GetAppStorekitConfigResponse423 | GetAppStorekitConfigResponse429 | GetAppStorekitConfigResponse500 | GetAppStorekitConfigResponse503 | StoreKitConfigFile]
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
    GetAppStorekitConfigResponse400
    | GetAppStorekitConfigResponse401
    | GetAppStorekitConfigResponse403
    | GetAppStorekitConfigResponse404
    | GetAppStorekitConfigResponse423
    | GetAppStorekitConfigResponse429
    | GetAppStorekitConfigResponse500
    | GetAppStorekitConfigResponse503
    | StoreKitConfigFile
    | None
):
    """Get the StoreKit configuration for an app

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
        GetAppStorekitConfigResponse400 | GetAppStorekitConfigResponse401 | GetAppStorekitConfigResponse403 | GetAppStorekitConfigResponse404 | GetAppStorekitConfigResponse423 | GetAppStorekitConfigResponse429 | GetAppStorekitConfigResponse500 | GetAppStorekitConfigResponse503 | StoreKitConfigFile
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            app_id=app_id,
            client=client,
        )
    ).parsed
