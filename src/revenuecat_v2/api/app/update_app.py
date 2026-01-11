from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app import App
from ...models.update_app_body import UpdateAppBody
from ...models.update_app_response_400 import UpdateAppResponse400
from ...models.update_app_response_401 import UpdateAppResponse401
from ...models.update_app_response_403 import UpdateAppResponse403
from ...models.update_app_response_404 import UpdateAppResponse404
from ...models.update_app_response_409 import UpdateAppResponse409
from ...models.update_app_response_422 import UpdateAppResponse422
from ...models.update_app_response_423 import UpdateAppResponse423
from ...models.update_app_response_429 import UpdateAppResponse429
from ...models.update_app_response_500 import UpdateAppResponse500
from ...models.update_app_response_503 import UpdateAppResponse503
from ...types import Response


def _get_kwargs(
    project_id: str,
    app_id: str,
    *,
    body: UpdateAppBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/apps/{app_id}".format(
            project_id=quote(str(project_id), safe=""),
            app_id=quote(str(app_id), safe=""),
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
    | UpdateAppResponse400
    | UpdateAppResponse401
    | UpdateAppResponse403
    | UpdateAppResponse404
    | UpdateAppResponse409
    | UpdateAppResponse422
    | UpdateAppResponse423
    | UpdateAppResponse429
    | UpdateAppResponse500
    | UpdateAppResponse503
    | None
):
    if response.status_code == 200:
        response_200 = App.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateAppResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateAppResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdateAppResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateAppResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdateAppResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = UpdateAppResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = UpdateAppResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = UpdateAppResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateAppResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateAppResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    App
    | UpdateAppResponse400
    | UpdateAppResponse401
    | UpdateAppResponse403
    | UpdateAppResponse404
    | UpdateAppResponse409
    | UpdateAppResponse422
    | UpdateAppResponse423
    | UpdateAppResponse429
    | UpdateAppResponse500
    | UpdateAppResponse503
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
    body: UpdateAppBody,
) -> Response[
    App
    | UpdateAppResponse400
    | UpdateAppResponse401
    | UpdateAppResponse403
    | UpdateAppResponse404
    | UpdateAppResponse409
    | UpdateAppResponse422
    | UpdateAppResponse423
    | UpdateAppResponse429
    | UpdateAppResponse500
    | UpdateAppResponse503
]:
    """Update an app

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.
        body (UpdateAppBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[App | UpdateAppResponse400 | UpdateAppResponse401 | UpdateAppResponse403 | UpdateAppResponse404 | UpdateAppResponse409 | UpdateAppResponse422 | UpdateAppResponse423 | UpdateAppResponse429 | UpdateAppResponse500 | UpdateAppResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        app_id=app_id,
        body=body,
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
    body: UpdateAppBody,
) -> (
    App
    | UpdateAppResponse400
    | UpdateAppResponse401
    | UpdateAppResponse403
    | UpdateAppResponse404
    | UpdateAppResponse409
    | UpdateAppResponse422
    | UpdateAppResponse423
    | UpdateAppResponse429
    | UpdateAppResponse500
    | UpdateAppResponse503
    | None
):
    """Update an app

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.
        body (UpdateAppBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        App | UpdateAppResponse400 | UpdateAppResponse401 | UpdateAppResponse403 | UpdateAppResponse404 | UpdateAppResponse409 | UpdateAppResponse422 | UpdateAppResponse423 | UpdateAppResponse429 | UpdateAppResponse500 | UpdateAppResponse503
    """

    return sync_detailed(
        project_id=project_id,
        app_id=app_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAppBody,
) -> Response[
    App
    | UpdateAppResponse400
    | UpdateAppResponse401
    | UpdateAppResponse403
    | UpdateAppResponse404
    | UpdateAppResponse409
    | UpdateAppResponse422
    | UpdateAppResponse423
    | UpdateAppResponse429
    | UpdateAppResponse500
    | UpdateAppResponse503
]:
    """Update an app

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.
        body (UpdateAppBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[App | UpdateAppResponse400 | UpdateAppResponse401 | UpdateAppResponse403 | UpdateAppResponse404 | UpdateAppResponse409 | UpdateAppResponse422 | UpdateAppResponse423 | UpdateAppResponse429 | UpdateAppResponse500 | UpdateAppResponse503]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        app_id=app_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAppBody,
) -> (
    App
    | UpdateAppResponse400
    | UpdateAppResponse401
    | UpdateAppResponse403
    | UpdateAppResponse404
    | UpdateAppResponse409
    | UpdateAppResponse422
    | UpdateAppResponse423
    | UpdateAppResponse429
    | UpdateAppResponse500
    | UpdateAppResponse503
    | None
):
    """Update an app

     This endpoint requires the following permission(s):
    <code>project_configuration:apps:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        app_id (str):  Example: app1ab2c3d4.
        body (UpdateAppBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        App | UpdateAppResponse400 | UpdateAppResponse401 | UpdateAppResponse403 | UpdateAppResponse404 | UpdateAppResponse409 | UpdateAppResponse422 | UpdateAppResponse423 | UpdateAppResponse429 | UpdateAppResponse500 | UpdateAppResponse503
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            app_id=app_id,
            client=client,
            body=body,
        )
    ).parsed
