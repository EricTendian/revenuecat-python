from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_project_response_400 import CreateProjectResponse400
from ...models.create_project_response_401 import CreateProjectResponse401
from ...models.create_project_response_403 import CreateProjectResponse403
from ...models.create_project_response_404 import CreateProjectResponse404
from ...models.create_project_response_409 import CreateProjectResponse409
from ...models.create_project_response_422 import CreateProjectResponse422
from ...models.create_project_response_423 import CreateProjectResponse423
from ...models.create_project_response_429 import CreateProjectResponse429
from ...models.create_project_response_500 import CreateProjectResponse500
from ...models.create_project_response_503 import CreateProjectResponse503
from ...models.project import Project
from ...models.project_create import ProjectCreate
from ...types import Response


def _get_kwargs(
    *,
    body: ProjectCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse403
    | CreateProjectResponse404
    | CreateProjectResponse409
    | CreateProjectResponse422
    | CreateProjectResponse423
    | CreateProjectResponse429
    | CreateProjectResponse500
    | CreateProjectResponse503
    | Project
    | None
):
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateProjectResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreateProjectResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateProjectResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreateProjectResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CreateProjectResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = CreateProjectResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = CreateProjectResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateProjectResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateProjectResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse403
    | CreateProjectResponse404
    | CreateProjectResponse409
    | CreateProjectResponse422
    | CreateProjectResponse423
    | CreateProjectResponse429
    | CreateProjectResponse500
    | CreateProjectResponse503
    | Project
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProjectCreate,
) -> Response[
    CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse403
    | CreateProjectResponse404
    | CreateProjectResponse409
    | CreateProjectResponse422
    | CreateProjectResponse423
    | CreateProjectResponse429
    | CreateProjectResponse500
    | CreateProjectResponse503
    | Project
]:
    """Creates a new project

     This endpoint requires the following permission(s):
    <code>project_configuration:projects:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        body (ProjectCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse403 | CreateProjectResponse404 | CreateProjectResponse409 | CreateProjectResponse422 | CreateProjectResponse423 | CreateProjectResponse429 | CreateProjectResponse500 | CreateProjectResponse503 | Project]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ProjectCreate,
) -> (
    CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse403
    | CreateProjectResponse404
    | CreateProjectResponse409
    | CreateProjectResponse422
    | CreateProjectResponse423
    | CreateProjectResponse429
    | CreateProjectResponse500
    | CreateProjectResponse503
    | Project
    | None
):
    """Creates a new project

     This endpoint requires the following permission(s):
    <code>project_configuration:projects:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        body (ProjectCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse403 | CreateProjectResponse404 | CreateProjectResponse409 | CreateProjectResponse422 | CreateProjectResponse423 | CreateProjectResponse429 | CreateProjectResponse500 | CreateProjectResponse503 | Project
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProjectCreate,
) -> Response[
    CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse403
    | CreateProjectResponse404
    | CreateProjectResponse409
    | CreateProjectResponse422
    | CreateProjectResponse423
    | CreateProjectResponse429
    | CreateProjectResponse500
    | CreateProjectResponse503
    | Project
]:
    """Creates a new project

     This endpoint requires the following permission(s):
    <code>project_configuration:projects:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        body (ProjectCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse403 | CreateProjectResponse404 | CreateProjectResponse409 | CreateProjectResponse422 | CreateProjectResponse423 | CreateProjectResponse429 | CreateProjectResponse500 | CreateProjectResponse503 | Project]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ProjectCreate,
) -> (
    CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse403
    | CreateProjectResponse404
    | CreateProjectResponse409
    | CreateProjectResponse422
    | CreateProjectResponse423
    | CreateProjectResponse429
    | CreateProjectResponse500
    | CreateProjectResponse503
    | Project
    | None
):
    """Creates a new project

     This endpoint requires the following permission(s):
    <code>project_configuration:projects:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        body (ProjectCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse403 | CreateProjectResponse404 | CreateProjectResponse409 | CreateProjectResponse422 | CreateProjectResponse423 | CreateProjectResponse429 | CreateProjectResponse500 | CreateProjectResponse503 | Project
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
