from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app import App
from ...models.app_create import AppCreate
from ...models.create_app_response_400 import CreateAppResponse400
from ...models.create_app_response_401 import CreateAppResponse401
from ...models.create_app_response_403 import CreateAppResponse403
from ...models.create_app_response_404 import CreateAppResponse404
from ...models.create_app_response_409 import CreateAppResponse409
from ...models.create_app_response_422 import CreateAppResponse422
from ...models.create_app_response_423 import CreateAppResponse423
from ...models.create_app_response_429 import CreateAppResponse429
from ...models.create_app_response_500 import CreateAppResponse500
from ...models.create_app_response_503 import CreateAppResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: AppCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/apps".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    App
    | CreateAppResponse400
    | CreateAppResponse401
    | CreateAppResponse403
    | CreateAppResponse404
    | CreateAppResponse409
    | CreateAppResponse422
    | CreateAppResponse423
    | CreateAppResponse429
    | CreateAppResponse500
    | CreateAppResponse503
    | None
):
    if response.status_code == 201:
        response_201 = App.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateAppResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateAppResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreateAppResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateAppResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreateAppResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CreateAppResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = CreateAppResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = CreateAppResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateAppResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateAppResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    App
    | CreateAppResponse400
    | CreateAppResponse401
    | CreateAppResponse403
    | CreateAppResponse404
    | CreateAppResponse409
    | CreateAppResponse422
    | CreateAppResponse423
    | CreateAppResponse429
    | CreateAppResponse500
    | CreateAppResponse503
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
    body: AppCreate,
) -> Response[
    App
    | CreateAppResponse400
    | CreateAppResponse401
    | CreateAppResponse403
    | CreateAppResponse404
    | CreateAppResponse409
    | CreateAppResponse422
    | CreateAppResponse423
    | CreateAppResponse429
    | CreateAppResponse500
    | CreateAppResponse503
]:
    """Create an App

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (AppCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[App | CreateAppResponse400 | CreateAppResponse401 | CreateAppResponse403 | CreateAppResponse404 | CreateAppResponse409 | CreateAppResponse422 | CreateAppResponse423 | CreateAppResponse429 | CreateAppResponse500 | CreateAppResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AppCreate,
) -> (
    App
    | CreateAppResponse400
    | CreateAppResponse401
    | CreateAppResponse403
    | CreateAppResponse404
    | CreateAppResponse409
    | CreateAppResponse422
    | CreateAppResponse423
    | CreateAppResponse429
    | CreateAppResponse500
    | CreateAppResponse503
    | None
):
    """Create an App

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (AppCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        App | CreateAppResponse400 | CreateAppResponse401 | CreateAppResponse403 | CreateAppResponse404 | CreateAppResponse409 | CreateAppResponse422 | CreateAppResponse423 | CreateAppResponse429 | CreateAppResponse500 | CreateAppResponse503
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AppCreate,
) -> Response[
    App
    | CreateAppResponse400
    | CreateAppResponse401
    | CreateAppResponse403
    | CreateAppResponse404
    | CreateAppResponse409
    | CreateAppResponse422
    | CreateAppResponse423
    | CreateAppResponse429
    | CreateAppResponse500
    | CreateAppResponse503
]:
    """Create an App

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (AppCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[App | CreateAppResponse400 | CreateAppResponse401 | CreateAppResponse403 | CreateAppResponse404 | CreateAppResponse409 | CreateAppResponse422 | CreateAppResponse423 | CreateAppResponse429 | CreateAppResponse500 | CreateAppResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AppCreate,
) -> (
    App
    | CreateAppResponse400
    | CreateAppResponse401
    | CreateAppResponse403
    | CreateAppResponse404
    | CreateAppResponse409
    | CreateAppResponse422
    | CreateAppResponse423
    | CreateAppResponse429
    | CreateAppResponse500
    | CreateAppResponse503
    | None
):
    """Create an App

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (AppCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        App | CreateAppResponse400 | CreateAppResponse401 | CreateAppResponse403 | CreateAppResponse404 | CreateAppResponse409 | CreateAppResponse422 | CreateAppResponse423 | CreateAppResponse429 | CreateAppResponse500 | CreateAppResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
