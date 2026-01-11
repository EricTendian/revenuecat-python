from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_app_public_api_keys_response_400 import ListAppPublicApiKeysResponse400
from ...models.list_app_public_api_keys_response_401 import ListAppPublicApiKeysResponse401
from ...models.list_app_public_api_keys_response_403 import ListAppPublicApiKeysResponse403
from ...models.list_app_public_api_keys_response_404 import ListAppPublicApiKeysResponse404
from ...models.list_app_public_api_keys_response_423 import ListAppPublicApiKeysResponse423
from ...models.list_app_public_api_keys_response_429 import ListAppPublicApiKeysResponse429
from ...models.list_app_public_api_keys_response_500 import ListAppPublicApiKeysResponse500
from ...models.list_app_public_api_keys_response_503 import ListAppPublicApiKeysResponse503
from ...models.public_api_key_list import PublicApiKeyList
from ...types import Response


def _get_kwargs(
    project_id: str,
    app_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/apps/{app_id}/public_api_keys".format(
            project_id=quote(str(project_id), safe=""),
            app_id=quote(str(app_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListAppPublicApiKeysResponse400
    | ListAppPublicApiKeysResponse401
    | ListAppPublicApiKeysResponse403
    | ListAppPublicApiKeysResponse404
    | ListAppPublicApiKeysResponse423
    | ListAppPublicApiKeysResponse429
    | ListAppPublicApiKeysResponse500
    | ListAppPublicApiKeysResponse503
    | PublicApiKeyList
    | None
):
    if response.status_code == 200:
        response_200 = PublicApiKeyList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListAppPublicApiKeysResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListAppPublicApiKeysResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListAppPublicApiKeysResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListAppPublicApiKeysResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = ListAppPublicApiKeysResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = ListAppPublicApiKeysResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListAppPublicApiKeysResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListAppPublicApiKeysResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListAppPublicApiKeysResponse400
    | ListAppPublicApiKeysResponse401
    | ListAppPublicApiKeysResponse403
    | ListAppPublicApiKeysResponse404
    | ListAppPublicApiKeysResponse423
    | ListAppPublicApiKeysResponse429
    | ListAppPublicApiKeysResponse500
    | ListAppPublicApiKeysResponse503
    | PublicApiKeyList
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
    ListAppPublicApiKeysResponse400
    | ListAppPublicApiKeysResponse401
    | ListAppPublicApiKeysResponse403
    | ListAppPublicApiKeysResponse404
    | ListAppPublicApiKeysResponse423
    | ListAppPublicApiKeysResponse429
    | ListAppPublicApiKeysResponse500
    | ListAppPublicApiKeysResponse503
    | PublicApiKeyList
]:
    """Get a list of the public API keys of an app

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
        Response[ListAppPublicApiKeysResponse400 | ListAppPublicApiKeysResponse401 | ListAppPublicApiKeysResponse403 | ListAppPublicApiKeysResponse404 | ListAppPublicApiKeysResponse423 | ListAppPublicApiKeysResponse429 | ListAppPublicApiKeysResponse500 | ListAppPublicApiKeysResponse503 | PublicApiKeyList]
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
    ListAppPublicApiKeysResponse400
    | ListAppPublicApiKeysResponse401
    | ListAppPublicApiKeysResponse403
    | ListAppPublicApiKeysResponse404
    | ListAppPublicApiKeysResponse423
    | ListAppPublicApiKeysResponse429
    | ListAppPublicApiKeysResponse500
    | ListAppPublicApiKeysResponse503
    | PublicApiKeyList
    | None
):
    """Get a list of the public API keys of an app

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
        ListAppPublicApiKeysResponse400 | ListAppPublicApiKeysResponse401 | ListAppPublicApiKeysResponse403 | ListAppPublicApiKeysResponse404 | ListAppPublicApiKeysResponse423 | ListAppPublicApiKeysResponse429 | ListAppPublicApiKeysResponse500 | ListAppPublicApiKeysResponse503 | PublicApiKeyList
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
    ListAppPublicApiKeysResponse400
    | ListAppPublicApiKeysResponse401
    | ListAppPublicApiKeysResponse403
    | ListAppPublicApiKeysResponse404
    | ListAppPublicApiKeysResponse423
    | ListAppPublicApiKeysResponse429
    | ListAppPublicApiKeysResponse500
    | ListAppPublicApiKeysResponse503
    | PublicApiKeyList
]:
    """Get a list of the public API keys of an app

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
        Response[ListAppPublicApiKeysResponse400 | ListAppPublicApiKeysResponse401 | ListAppPublicApiKeysResponse403 | ListAppPublicApiKeysResponse404 | ListAppPublicApiKeysResponse423 | ListAppPublicApiKeysResponse429 | ListAppPublicApiKeysResponse500 | ListAppPublicApiKeysResponse503 | PublicApiKeyList]
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
    ListAppPublicApiKeysResponse400
    | ListAppPublicApiKeysResponse401
    | ListAppPublicApiKeysResponse403
    | ListAppPublicApiKeysResponse404
    | ListAppPublicApiKeysResponse423
    | ListAppPublicApiKeysResponse429
    | ListAppPublicApiKeysResponse500
    | ListAppPublicApiKeysResponse503
    | PublicApiKeyList
    | None
):
    """Get a list of the public API keys of an app

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
        ListAppPublicApiKeysResponse400 | ListAppPublicApiKeysResponse401 | ListAppPublicApiKeysResponse403 | ListAppPublicApiKeysResponse404 | ListAppPublicApiKeysResponse423 | ListAppPublicApiKeysResponse429 | ListAppPublicApiKeysResponse500 | ListAppPublicApiKeysResponse503 | PublicApiKeyList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            app_id=app_id,
            client=client,
        )
    ).parsed
